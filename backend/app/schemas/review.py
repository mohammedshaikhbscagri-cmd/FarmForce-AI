import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator


class ReviewCreate(BaseModel):
    booking_id: uuid.UUID
    rating: int
    comment: Optional[str] = None

    @field_validator("rating")
    @classmethod
    def rating_must_be_1_to_5(cls, v: int) -> int:
        if not 1 <= v <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return v


class ReviewResponse(BaseModel):
    id: uuid.UUID
    booking_id: uuid.UUID
    reviewer_id: uuid.UUID
    reviewee_id: uuid.UUID
    rating: int
    comment: Optional[str] = None
    reviewer_name: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}
