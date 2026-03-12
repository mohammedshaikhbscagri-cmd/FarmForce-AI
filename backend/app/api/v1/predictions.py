import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db
from app.services.prediction_service import PredictionService
from app.utils.constants import TaskType

router = APIRouter()
prediction_service = PredictionService()


@router.get("/labor-demand")
async def labor_demand(
    farm_id: uuid.UUID = Query(...),
    db: AsyncSession = Depends(get_db),
):
    """Return 7-day labor demand forecast for a farm."""
    forecast = prediction_service.predict_labor_demand(str(farm_id))
    return {"farm_id": str(farm_id), "forecast": forecast}


@router.get("/wage-suggestion")
async def wage_suggestion(
    task_type: TaskType = Query(...),
    district: str = Query(...),
):
    """Return wage suggestion for a task type in a district."""
    return prediction_service.suggest_wage(task_type.value, district)
