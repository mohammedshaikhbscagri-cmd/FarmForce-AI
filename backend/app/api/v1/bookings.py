import uuid
from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user, require_worker
from app.schemas.booking import BookingCreate, BookingResponse, CheckInRequest
from app.models.booking import Booking
from app.models.job import Job
from app.models.user import User
from app.utils.constants import BookingStatus, UserRole

router = APIRouter()


@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(
    body: BookingCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_worker),
):
    booking = Booking(job_id=body.job_id, worker_id=current_user.id)
    db.add(booking)
    await db.flush()
    await db.refresh(booking)
    return booking


@router.get("/", response_model=List[BookingResponse])
async def list_bookings(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role == UserRole.WORKER:
        query = select(Booking).where(Booking.worker_id == current_user.id)
    else:
        query = (
            select(Booking)
            .join(Job, Booking.job_id == Job.id)
            .where(Job.farmer_id == current_user.id)
        )
    result = await db.execute(query)
    return result.scalars().all()


@router.put("/{booking_id}/check-in", response_model=BookingResponse)
async def check_in(
    booking_id: uuid.UUID,
    body: CheckInRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_worker),
):
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    booking = result.scalar_one_or_none()
    if not booking or booking.worker_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    booking.status = BookingStatus.CHECKED_IN
    booking.check_in_time = datetime.utcnow()
    booking.check_in_lat = body.latitude
    booking.check_in_lng = body.longitude
    await db.flush()
    await db.refresh(booking)
    return booking


@router.put("/{booking_id}/check-out", response_model=BookingResponse)
async def check_out(
    booking_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_worker),
):
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    booking = result.scalar_one_or_none()
    if not booking or booking.worker_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    booking.check_out_time = datetime.utcnow()
    await db.flush()
    await db.refresh(booking)
    return booking


@router.put("/{booking_id}/confirm", response_model=BookingResponse)
async def confirm_booking(
    booking_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(Booking).join(Job, Booking.job_id == Job.id).where(Booking.id == booking_id)
    )
    booking = result.scalar_one_or_none()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    booking.farmer_confirmed = True
    booking.status = BookingStatus.COMPLETED
    await db.flush()
    await db.refresh(booking)
    return booking


@router.put("/{booking_id}/cancel", response_model=BookingResponse)
async def cancel_booking(
    booking_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    booking = result.scalar_one_or_none()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")
    booking.status = BookingStatus.CANCELLED
    await db.flush()
    await db.refresh(booking)
    return booking
