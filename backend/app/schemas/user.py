import uuid
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

from app.utils.constants import UserRole, SkillType


class UserCreate(BaseModel):
    phone: str
    role: UserRole
    name: str
    language_pref: str = "hi"


class UserUpdate(BaseModel):
    name: Optional[str] = None
    village: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    language_pref: Optional[str] = None
    upi_id: Optional[str] = None
    profile_photo_url: Optional[str] = None


class UserResponse(BaseModel):
    id: uuid.UUID
    phone: str
    role: UserRole
    name: Optional[str] = None
    village: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    language_pref: str
    avg_rating: float
    total_jobs: int
    is_verified: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class FarmCreate(BaseModel):
    location_lat: float
    location_lng: float
    farm_size_acres: float
    crops: List[str]
    soil_type: Optional[str] = None


class SkillItem(BaseModel):
    skill_type: SkillType
    experience_years: int = 0


class SkillUpdate(BaseModel):
    skills: List[SkillItem]
