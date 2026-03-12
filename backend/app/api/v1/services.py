from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user
from app.models.service import Service
from app.models.user import User
from app.utils.geo import haversine_distance
from app.utils.constants import ServiceType

router = APIRouter()


@router.get("/nearby")
async def nearby_services(
    latitude: float = Query(...),
    longitude: float = Query(...),
    max_distance_km: float = Query(50),
    service_type: Optional[ServiceType] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    """Return services within the given radius."""
    query = select(Service).where(Service.availability_status == True)
    if service_type:
        query = query.where(Service.service_type == service_type)
    result = await db.execute(query)
    services = result.scalars().all()

    nearby = []
    for svc in services:
        dist = haversine_distance(latitude, longitude, svc.location_lat, svc.location_lng)
        if dist <= max_distance_km:
            nearby.append({
                "id": str(svc.id),
                "service_type": svc.service_type,
                "price_per_acre": float(svc.price_per_acre),
                "distance_km": round(dist, 2),
                "avg_rating": svc.avg_rating,
                "description": svc.description,
            })
    return sorted(nearby, key=lambda x: x["distance_km"])


@router.post("/book")
async def book_service(
    service_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Book a service (drone, tractor, etc.)."""
    # TODO: Implement full service booking flow
    return {"message": "Service booking request received", "service_id": service_id}
