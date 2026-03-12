from typing import List
from app.utils.geo import haversine_distance
from app.utils.constants import MAX_SEARCH_RADIUS_KM


class MatchingService:
    """AI-powered worker-job matching engine using a weighted scoring model."""

    WEIGHTS = {
        "distance": 0.35,
        "skill": 0.30,
        "rating": 0.20,
        "reliability": 0.15,
    }

    def _distance_score(self, worker, job) -> float:
        """Score 40 points max — higher for closer workers (max 40 km)."""
        dist = haversine_distance(
            worker.location_lat if hasattr(worker, "location_lat") else 0,
            worker.location_lng if hasattr(worker, "location_lng") else 0,
            job.location_lat,
            job.location_lng,
        )
        if dist >= MAX_SEARCH_RADIUS_KM:
            return 0.0
        return max(0.0, 40.0 * (1 - dist / MAX_SEARCH_RADIUS_KM))

    def _skill_score(self, worker, job) -> float:
        """Score 30 points max based on skill match."""
        if not hasattr(worker, "skills") or not worker.skills:
            return 0.0
        skill_types = {s.skill_type.value if hasattr(s.skill_type, "value") else s.skill_type for s in worker.skills}
        job_task = job.task_type.value if hasattr(job.task_type, "value") else job.task_type
        if job_task in skill_types:
            return 30.0
        # Related skills get partial score
        related = {"SOWING", "TRANSPLANTING", "WEEDING"}
        if job_task in related and skill_types & related:
            return 15.0
        return 0.0

    def _rating_score(self, worker) -> float:
        """Score 20 points max proportional to average rating."""
        return (getattr(worker, "avg_rating", 0.0) / 5.0) * 20.0

    def _reliability_score(self, worker) -> float:
        """Score 10 points max based on job completion ratio."""
        total = getattr(worker, "total_jobs", 0)
        if total == 0:
            return 5.0
        completed = len([b for b in getattr(worker, "bookings_as_worker", []) if getattr(b, "status", "") == "COMPLETED"])
        return (completed / total) * 10.0

    def score_worker(self, worker, job) -> float:
        """Calculate composite match score (0–100)."""
        return (
            self._distance_score(worker, job)
            + self._skill_score(worker, job)
            + self._rating_score(worker)
            + self._reliability_score(worker)
        )

    def rank_workers(self, workers: List, job) -> List:
        """Return workers sorted by match score (descending)."""
        scored = [(w, self.score_worker(w, job)) for w in workers]
        return [w for w, _ in sorted(scored, key=lambda x: x[1], reverse=True)]

    def rank_jobs(self, jobs: List, worker) -> List:
        """Return jobs sorted by relevance to a worker (descending)."""
        scored = [(j, self._skill_score(worker, j) + self._rating_score(worker)) for j in jobs]
        return [j for j, _ in sorted(scored, key=lambda x: x[1], reverse=True)]
