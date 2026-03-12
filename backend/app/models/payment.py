import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import String, Numeric, DateTime, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.models import Base
from app.utils.constants import PaymentStatus, PaymentMode


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    booking_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("bookings.id"), nullable=False)
    farmer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    worker_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    platform_commission: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    worker_payout: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(SAEnum(PaymentStatus), default=PaymentStatus.PENDING)
    razorpay_order_id: Mapped[str] = mapped_column(String(255), nullable=True)
    razorpay_payment_id: Mapped[str] = mapped_column(String(255), nullable=True)
    razorpay_transfer_id: Mapped[str] = mapped_column(String(255), nullable=True)
    payment_mode: Mapped[str] = mapped_column(SAEnum(PaymentMode), default=PaymentMode.UPI)
    paid_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    booking = relationship("Booking", back_populates="payment")
