import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.utils.constants import BookingStatus


class BookingCreate(BaseModel):
    job_id: uuid.UUID
    worker_id: uuid.UUID


class BookingResponse(BaseModel):
    id: uuid.UUID
    job_id: uuid.UUID
    worker_id: uuid.UUID
    status: BookingStatus
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    check_in_lat: Optional[float] = None
    check_in_lng: Optional[float] = None
    farmer_confirmed: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class CheckInRequest(BaseModel):
    latitude: float
    longitude: float
