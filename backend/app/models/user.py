import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, Float, Integer, DateTime, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.models import Base
from app.utils.constants import UserRole


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phone: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(SAEnum(UserRole), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    village: Mapped[str] = mapped_column(String(255), nullable=True)
    district: Mapped[str] = mapped_column(String(255), nullable=True)
    state: Mapped[str] = mapped_column(String(255), nullable=True)
    language_pref: Mapped[str] = mapped_column(String(10), default="hi")
    aadhaar_hash: Mapped[str] = mapped_column(String(64), nullable=True)
    upi_id: Mapped[str] = mapped_column(String(255), nullable=True)
    profile_photo_url: Mapped[str] = mapped_column(String(500), nullable=True)
    avg_rating: Mapped[float] = mapped_column(Float, default=0.0)
    total_jobs: Mapped[int] = mapped_column(Integer, default=0)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)

    jobs = relationship("Job", back_populates="farmer", foreign_keys="Job.farmer_id")
    bookings_as_worker = relationship("Booking", back_populates="worker", foreign_keys="Booking.worker_id")
    skills = relationship("WorkerSkill", back_populates="worker")
    farms = relationship("FarmerFarm", back_populates="farmer")
    reviews_given = relationship("Review", back_populates="reviewer", foreign_keys="Review.reviewer_id")
    reviews_received = relationship("Review", back_populates="reviewee", foreign_keys="Review.reviewee_id")
