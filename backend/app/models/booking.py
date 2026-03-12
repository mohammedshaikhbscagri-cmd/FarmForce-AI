import uuid
from datetime import datetime
from sqlalchemy import Boolean, Float, DateTime, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.models import Base
from app.utils.constants import BookingStatus


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    worker_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    status: Mapped[str] = mapped_column(SAEnum(BookingStatus), default=BookingStatus.PENDING)
    check_in_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    check_out_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    check_in_lat: Mapped[float] = mapped_column(Float, nullable=True)
    check_in_lng: Mapped[float] = mapped_column(Float, nullable=True)
    farmer_confirmed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)

    job = relationship("Job", back_populates="bookings")
    worker = relationship("User", back_populates="bookings_as_worker", foreign_keys=[worker_id])
    payment = relationship("Payment", back_populates="booking", uselist=False)
    review = relationship("Review", back_populates="booking", uselist=False)
