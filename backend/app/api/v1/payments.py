import uuid
from typing import List
from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user, require_farmer
from app.schemas.payment import CreateOrderRequest, CreateOrderResponse, VerifyPaymentRequest, PaymentResponse
from app.models.payment import Payment
from app.models.booking import Booking
from app.models.user import User
from app.services.payment_service import PaymentService
from app.utils.constants import PaymentStatus

router = APIRouter()
payment_service = PaymentService()


@router.post("/create-order", response_model=CreateOrderResponse)
async def create_order(
    body: CreateOrderRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_farmer),
):
    result = await db.execute(
        select(Booking).where(Booking.id == body.booking_id)
    )
    booking = result.scalar_one_or_none()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

    job_result = await db.execute(
        select(__import__("app.models.job", fromlist=["Job"]).Job).where(
            __import__("app.models.job", fromlist=["Job"]).Job.id == booking.job_id
        )
    )
    job = job_result.scalar_one_or_none()
    amount = job.wage_per_day if job else Decimal("300")

    order = payment_service.create_order(amount, str(body.booking_id))

    commission = amount * Decimal(str(0.075))
    worker_payout = amount - commission

    payment = Payment(
        booking_id=booking.id,
        farmer_id=current_user.id,
        worker_id=booking.worker_id,
        amount=amount,
        platform_commission=commission,
        worker_payout=worker_payout,
        razorpay_order_id=order["id"],
    )
    db.add(payment)
    await db.flush()

    return CreateOrderResponse(
        razorpay_order_id=order["id"],
        amount=amount,
        currency="INR",
    )


@router.post("/verify")
async def verify_payment(
    body: VerifyPaymentRequest,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Payment).where(Payment.razorpay_order_id == body.razorpay_order_id)
    )
    payment = result.scalar_one_or_none()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

    try:
        payment_service.verify_payment(
            body.razorpay_order_id, body.razorpay_payment_id, body.razorpay_signature
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    payment.status = PaymentStatus.HELD_IN_ESCROW
    payment.razorpay_payment_id = body.razorpay_payment_id
    await db.flush()
    return {"message": "Payment verified and held in escrow"}


@router.post("/{payment_id}/release")
async def release_payment(
    payment_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Payment).where(Payment.id == payment_id))
    payment = result.scalar_one_or_none()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

    worker_result = await db.execute(
        select(User).where(User.id == payment.worker_id)
    )
    worker = worker_result.scalar_one_or_none()
    transfer = payment_service.release_to_worker(
        str(payment.razorpay_payment_id or payment.id),
        worker.upi_id if worker and worker.upi_id else "",
        payment.worker_payout,
    )
    payment.status = PaymentStatus.RELEASED
    payment.razorpay_transfer_id = transfer["transfer_id"]
    await db.flush()
    return {"message": "Payment released to worker", "transfer": transfer}


@router.get("/history", response_model=List[PaymentResponse])
async def payment_history(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    from app.utils.constants import UserRole
    if current_user.role == UserRole.FARMER:
        query = select(Payment).where(Payment.farmer_id == current_user.id)
    else:
        query = select(Payment).where(Payment.worker_id == current_user.id)
    result = await db.execute(query)
    return result.scalars().all()
