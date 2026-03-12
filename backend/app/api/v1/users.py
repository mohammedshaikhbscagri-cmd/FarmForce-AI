import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user, require_farmer, require_worker
from app.schemas.user import UserResponse, UserUpdate, FarmCreate, SkillUpdate
from app.models.user import User
from app.models.farm import FarmerFarm
from app.models.skill import WorkerSkill

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserResponse)
async def update_me(
    body: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    for field, value in body.model_dump(exclude_none=True).items():
        setattr(current_user, field, value)
    db.add(current_user)
    await db.flush()
    await db.refresh(current_user)
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/me/farm")
async def add_farm(
    body: FarmCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_farmer),
):
    farm = FarmerFarm(
        farmer_id=current_user.id,
        location_lat=body.location_lat,
        location_lng=body.location_lng,
        farm_size_acres=body.farm_size_acres,
        crops=",".join(body.crops),
        soil_type=body.soil_type,
    )
    db.add(farm)
    await db.flush()
    await db.refresh(farm)
    return {"id": str(farm.id), "message": "Farm added"}


@router.put("/me/skills")
async def update_skills(
    body: SkillUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_worker),
):
    result = await db.execute(select(WorkerSkill).where(WorkerSkill.worker_id == current_user.id))
    existing = result.scalars().all()
    for skill in existing:
        await db.delete(skill)
    new_skills = []
    for item in body.skills:
        skill = WorkerSkill(
            worker_id=current_user.id,
            skill_type=item.skill_type,
            experience_years=item.experience_years,
        )
        db.add(skill)
        new_skills.append(skill)
    await db.flush()
    return {"message": "Skills updated", "count": len(new_skills)}
