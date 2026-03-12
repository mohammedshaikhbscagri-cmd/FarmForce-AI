import uuid
from sqlalchemy import Integer, Boolean, Enum as SAEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.models import Base
from app.utils.constants import SkillType, BadgeLevel


class WorkerSkill(Base):
    __tablename__ = "worker_skills"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    worker_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    skill_type: Mapped[str] = mapped_column(SAEnum(SkillType), nullable=False)
    experience_years: Mapped[int] = mapped_column(Integer, default=0)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    badge_level: Mapped[str] = mapped_column(SAEnum(BadgeLevel), default=BadgeLevel.NONE)

    worker = relationship("User", back_populates="skills")
