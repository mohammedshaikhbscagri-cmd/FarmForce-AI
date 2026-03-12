import uuid
from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db
from app.models.user import User
from app.models.job import Job
from app.services.matching_service import MatchingService
from app.utils.constants import JobStatus, UserRole

router = APIRouter()
matching_service = MatchingService()


@router.get("/workers")
async def match_workers_for_job(
    job_id: uuid.UUID = Query(...),
    db: AsyncSession = Depends(get_db),
):
    """Return a ranked list of workers for a given job."""
    result = await db.execute(select(Job).where(Job.id == job_id))
    job = result.scalar_one_or_none()
    if not job:
        return []

    workers_result = await db.execute(
        select(User).where(User.role == UserRole.WORKER, User.is_active == True)
    )
    workers = workers_result.scalars().all()
    ranked = matching_service.rank_workers(workers, job)
    return [{"worker_id": str(w.id), "name": w.name, "avg_rating": w.avg_rating} for w in ranked[:20]]


@router.get("/jobs")
async def match_jobs_for_worker(
    worker_id: uuid.UUID = Query(...),
    db: AsyncSession = Depends(get_db),
):
    """Return a ranked list of jobs for a given worker."""
    result = await db.execute(select(User).where(User.id == worker_id))
    worker = result.scalar_one_or_none()
    if not worker:
        return []

    jobs_result = await db.execute(
        select(Job).where(Job.status == JobStatus.OPEN)
    )
    jobs = jobs_result.scalars().all()
    ranked = matching_service.rank_jobs(jobs, worker)
    return [{"job_id": str(j.id), "task_type": j.task_type, "wage_per_day": float(j.wage_per_day)} for j in ranked[:20]]
