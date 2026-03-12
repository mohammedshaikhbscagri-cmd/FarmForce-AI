import uuid
from datetime import datetime, date
from decimal import Decimal
from sqlalchemy import String, Integer, Numeric, Date, Float, Text, DateTime, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.models import Base
from app.utils.constants import TaskType, JobStatus, UrgencyLevel


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    farmer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    task_type: Mapped[str] = mapped_column(SAEnum(TaskType), nullable=False)
    crop_type: Mapped[str] = mapped_column(String(255), nullable=False)
    workers_needed: Mapped[int] = mapped_column(Integer, nullable=False)
    wage_per_day: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    location_lat: Mapped[float] = mapped_column(Float, nullable=False)
    location_lng: Mapped[float] = mapped_column(Float, nullable=False)
    village: Mapped[str] = mapped_column(String(255), nullable=False)
    district: Mapped[str] = mapped_column(String(255), nullable=False)
    state: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(SAEnum(JobStatus), default=JobStatus.OPEN)
    urgency: Mapped[str] = mapped_column(SAEnum(UrgencyLevel), default=UrgencyLevel.NORMAL)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)

    farmer = relationship("User", back_populates="jobs", foreign_keys=[farmer_id])
    bookings = relationship("Booking", back_populates="job")
