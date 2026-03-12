import uuid
from typing import List, Optional
from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user, require_farmer
from app.schemas.job import JobCreate, JobUpdate, JobResponse
from app.models.job import Job
from app.models.user import User
from app.services.voice_service import VoiceService
from app.utils.constants import JobStatus, TaskType

router = APIRouter()
voice_service = VoiceService()


@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
async def create_job(
    body: JobCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_farmer),
):
    job = Job(farmer_id=current_user.id, **body.model_dump())
    db.add(job)
    await db.flush()
    await db.refresh(job)
    return job


@router.get("/", response_model=List[JobResponse])
async def list_jobs(
    task_type: Optional[TaskType] = Query(None),
    min_wage: Optional[Decimal] = Query(None),
    district: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    query = select(Job).where(Job.status == JobStatus.OPEN)
    if task_type:
        query = query.where(Job.task_type == task_type)
    if min_wage:
        query = query.where(Job.wage_per_day >= min_wage)
    if district:
        query = query.where(Job.district == district)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/my-jobs", response_model=List[JobResponse])
async def my_jobs(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_farmer),
):
    result = await db.execute(select(Job).where(Job.farmer_id == current_user.id))
    return result.scalars().all()


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return job


@router.put("/{job_id}", response_model=JobResponse)
async def update_job(
    job_id: uuid.UUID,
    body: JobUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if job.farmer_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    for field, value in body.model_dump(exclude_none=True).items():
        setattr(job, field, value)
    await db.flush()
    await db.refresh(job)
    return job


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
async def cancel_job(
    job_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    if job.farmer_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    job.status = JobStatus.CANCELLED
    await db.flush()


@router.post("/voice", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
async def create_job_from_voice(
    audio_file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_farmer),
):
    """Parse an audio file and create a job from the voice input."""
    import tempfile, os
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        content = await audio_file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        parsed = voice_service.parse_voice_to_job(tmp_path, language="hi")
    finally:
        os.unlink(tmp_path)

    from datetime import date, timedelta
    job = Job(
        farmer_id=current_user.id,
        task_type=parsed.get("task_type", "OTHER"),
        crop_type=parsed.get("crop_type", "Other"),
        workers_needed=parsed.get("workers_needed", 1),
        wage_per_day=parsed.get("wage_per_day", 300),
        start_date=date.today() + timedelta(days=1),
        end_date=date.today() + timedelta(days=2),
        location_lat=0.0,
        location_lng=0.0,
        village="",
        district="",
        state="",
    )
    db.add(job)
    await db.flush()
    await db.refresh(job)
    return job
