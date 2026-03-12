"""
Feature engineering functions for the matching model.
"""
import math
from typing import List, Dict


def compute_distance_features(worker: Dict, job: Dict) -> Dict:
    """Compute distance-related features between a worker and job."""
    lat1, lng1 = worker.get("lat", 0), worker.get("lng", 0)
    lat2, lng2 = job.get("lat", 0), job.get("lng", 0)

    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    distance_km = R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return {
        "distance_km": distance_km,
        "is_within_15km": distance_km <= 15,
        "is_within_50km": distance_km <= 50,
        "same_district": worker.get("district") == job.get("district"),
        "same_state": worker.get("state") == job.get("state"),
    }


def compute_skill_features(worker: Dict, job: Dict) -> Dict:
    """Compute skill overlap features."""
    worker_skills = set(worker.get("skills", []))
    job_task = job.get("task_type", "")
    return {
        "has_exact_skill": job_task in worker_skills,
        "skill_count": len(worker_skills),
        "years_experience": max(
            (s.get("experience_years", 0) for s in worker.get("skill_details", [])), default=0
        ),
    }


def compute_temporal_features(job: Dict) -> Dict:
    """Compute time-based features for a job."""
    import datetime
    today = datetime.date.today()
    start_date = job.get("start_date")
    if isinstance(start_date, str):
        start_date = datetime.date.fromisoformat(start_date)
    days_until_start = (start_date - today).days if start_date else 0

    return {
        "days_until_start": max(0, days_until_start),
        "is_urgent": job.get("urgency") == "URGENT",
        "duration_days": (
            (datetime.date.fromisoformat(str(job.get("end_date"))) - datetime.date.fromisoformat(str(job.get("start_date")))).days
            if job.get("start_date") and job.get("end_date") else 1
        ),
    }
