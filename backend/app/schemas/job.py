import uuid
from datetime import datetime, date
from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel

from app.utils.constants import TaskType, JobStatus, UrgencyLevel


class JobCreate(BaseModel):
    task_type: TaskType
    crop_type: str
    workers_needed: int
    wage_per_day: Decimal
    start_date: date
    end_date: date
    location_lat: float
    location_lng: float
    village: str
    district: str
    state: str
    urgency: UrgencyLevel = UrgencyLevel.NORMAL
    description: Optional[str] = None


class JobUpdate(BaseModel):
    workers_needed: Optional[int] = None
    wage_per_day: Optional[Decimal] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    description: Optional[str] = None
    status: Optional[JobStatus] = None


class JobResponse(BaseModel):
    id: uuid.UUID
    farmer_id: uuid.UUID
    task_type: TaskType
    crop_type: str
    workers_needed: int
    wage_per_day: Decimal
    start_date: date
    end_date: date
    location_lat: float
    location_lng: float
    village: str
    district: str
    state: str
    status: JobStatus
    urgency: UrgencyLevel
    description: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class JobFilter(BaseModel):
    task_type: Optional[TaskType] = None
    min_wage: Optional[Decimal] = None
    max_distance_km: Optional[float] = None
    date: Optional[date] = None
    district: Optional[str] = None


class VoiceJobRequest(BaseModel):
    audio_url: str
    language: str = "hi"
