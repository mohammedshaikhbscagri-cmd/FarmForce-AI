import uuid
from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

from app.utils.constants import PaymentStatus, PaymentMode


class CreateOrderRequest(BaseModel):
    booking_id: uuid.UUID


class CreateOrderResponse(BaseModel):
    razorpay_order_id: str
    amount: Decimal
    currency: str = "INR"


class VerifyPaymentRequest(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str


class PaymentResponse(BaseModel):
    id: uuid.UUID
    booking_id: uuid.UUID
    farmer_id: uuid.UUID
    worker_id: uuid.UUID
    amount: Decimal
    platform_commission: Decimal
    worker_payout: Decimal
    status: PaymentStatus
    razorpay_order_id: Optional[str] = None
    razorpay_payment_id: Optional[str] = None
    payment_mode: PaymentMode
    paid_at: Optional[datetime] = None
    created_at: datetime

    model_config = {"from_attributes": True}
