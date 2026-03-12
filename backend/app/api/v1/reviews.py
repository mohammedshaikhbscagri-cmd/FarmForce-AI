import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user
from app.schemas.review import ReviewCreate, ReviewResponse
from app.models.review import Review
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(
    body: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    from app.models.booking import Booking
    result = await db.execute(select(Booking).where(Booking.id == body.booking_id))
    booking = result.scalar_one_or_none()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found")

    reviewee_id = booking.worker_id if current_user.id == booking.job_id else booking.worker_id

    review = Review(
        booking_id=body.booking_id,
        reviewer_id=current_user.id,
        reviewee_id=reviewee_id,
        rating=body.rating,
        comment=body.comment,
    )
    db.add(review)
    await db.flush()
    await db.refresh(review)

    reviewer_result = await db.execute(select(User).where(User.id == review.reviewer_id))
    reviewer = reviewer_result.scalar_one_or_none()

    return ReviewResponse(
        id=review.id,
        booking_id=review.booking_id,
        reviewer_id=review.reviewer_id,
        reviewee_id=review.reviewee_id,
        rating=review.rating,
        comment=review.comment,
        reviewer_name=reviewer.name if reviewer else None,
        created_at=review.created_at,
    )


@router.get("/user/{user_id}", response_model=List[ReviewResponse])
async def get_user_reviews(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Review).where(Review.reviewee_id == user_id))
    reviews = result.scalars().all()
    responses = []
    for review in reviews:
        reviewer_result = await db.execute(select(User).where(User.id == review.reviewer_id))
        reviewer = reviewer_result.scalar_one_or_none()
        responses.append(ReviewResponse(
            id=review.id,
            booking_id=review.booking_id,
            reviewer_id=review.reviewer_id,
            reviewee_id=review.reviewee_id,
            rating=review.rating,
            comment=review.comment,
            reviewer_name=reviewer.name if reviewer else None,
            created_at=review.created_at,
        ))
    return responses
