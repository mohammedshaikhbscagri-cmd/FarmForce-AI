import pytest
from app.services.matching_service import MatchingService


class MockWorker:
    def __init__(self):
        self.id = "worker-1"
        self.name = "Ramesh"
        self.avg_rating = 4.5
        self.total_jobs = 10
        self.bookings_as_worker = []
        self.skills = []
        self.location_lat = 18.52
        self.location_lng = 73.85


class MockJob:
    def __init__(self):
        self.task_type = "HARVESTING"
        self.location_lat = 18.52
        self.location_lng = 73.86


def test_score_worker():
    service = MatchingService()
    worker = MockWorker()
    job = MockJob()
    score = service.score_worker(worker, job)
    assert 0 <= score <= 100


def test_rank_workers():
    service = MatchingService()
    workers = [MockWorker(), MockWorker()]
    job = MockJob()
    ranked = service.rank_workers(workers, job)
    assert len(ranked) == 2
