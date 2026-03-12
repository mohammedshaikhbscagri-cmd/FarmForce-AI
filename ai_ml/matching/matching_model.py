"""
AI-powered worker-job matching engine using a weighted scoring model.
"""
from typing import List, Dict, Any
import math


class MatchingEngine:
    """AI-powered worker-job matching engine."""

    WEIGHTS = {
        "distance": 0.35,
        "skill_match": 0.30,
        "rating": 0.20,
        "reliability": 0.15,
    }

    MAX_DISTANCE_KM = 50.0

    def _haversine(self, lat1: float, lng1: float, lat2: float, lng2: float) -> float:
        """Calculate distance in km using the Haversine formula."""
        R = 6371.0
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lng2 - lng1)
        a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    def _distance_score(self, worker: Dict, job: Dict) -> float:
        """100 if <1km, 0 if >50km, linear interpolation between."""
        dist = self._haversine(
            worker.get("lat", 0), worker.get("lng", 0),
            job.get("lat", 0), job.get("lng", 0),
        )
        if dist >= self.MAX_DISTANCE_KM:
            return 0.0
        if dist <= 1.0:
            return 100.0
        return max(0.0, 100.0 * (1 - (dist - 1) / (self.MAX_DISTANCE_KM - 1)))

    def _skill_score(self, worker: Dict, job: Dict) -> float:
        """100 if exact skill match, 50 if related skill, 0 if none."""
        worker_skills = set(worker.get("skills", []))
        job_task = job.get("task_type", "")
        if job_task in worker_skills:
            return 100.0
        # Check related skills
        related_groups = [
            {"SOWING", "TRANSPLANTING"},
            {"WEEDING", "PRUNING"},
            {"MANUAL_SPRAYING", "MACHINE_SPRAYING"},
            {"PADDY_HARVESTING", "COTTON_PICKING", "GRAPE_HARVESTING", "SUGARCANE_CUTTING"},
        ]
        for group in related_groups:
            if job_task in group and worker_skills & group:
                return 50.0
        return 0.0

    def _rating_score(self, worker: Dict) -> float:
        """Proportional to avg rating: (rating / 5.0) * 100."""
        return (worker.get("avg_rating", 0.0) / 5.0) * 100.0

    def _reliability_score(self, worker: Dict) -> float:
        """(completed_jobs / total_bookings) * 100. Default 50 if no history."""
        total = worker.get("total_bookings", 0)
        if total == 0:
            return 50.0
        completed = worker.get("completed_jobs", 0)
        return (completed / total) * 100.0

    def score_worker(self, worker: Dict, job: Dict) -> float:
        """Calculate composite match score (0–100)."""
        return (
            self.WEIGHTS["distance"] * self._distance_score(worker, job)
            + self.WEIGHTS["skill_match"] * self._skill_score(worker, job)
            + self.WEIGHTS["rating"] * self._rating_score(worker)
            + self.WEIGHTS["reliability"] * self._reliability_score(worker)
        )

    def rank_workers(self, workers: List[Dict], job: Dict) -> List[Dict]:
        """Rank all workers by match score for a job (descending)."""
        scored = [(w, self.score_worker(w, job)) for w in workers]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [{"worker": w, "match_score": round(s, 2)} for w, s in scored]

    def rank_jobs(self, jobs: List[Dict], worker: Dict) -> List[Dict]:
        """Rank all jobs by match score for a worker (descending)."""
        scored = [(j, self.score_worker(worker, j)) for j in jobs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [{"job": j, "match_score": round(s, 2)} for j, s in scored]
