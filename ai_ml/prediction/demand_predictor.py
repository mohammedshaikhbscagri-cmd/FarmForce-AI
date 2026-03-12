"""
Labor demand predictor for farms using crop stage + weather + historical patterns.
"""
import datetime
from typing import List, Dict, Any


class LaborDemandPredictor:
    """Predict labor demand for a farm over the next N days."""

    # Historical average workers needed by crop stage
    CROP_STAGE_BASELINE = {
        "sowing": 5,
        "transplanting": 8,
        "weeding": 4,
        "spraying": 3,
        "harvesting": 10,
        "threshing": 6,
        "loading": 4,
        "idle": 1,
    }

    def predict(
        self,
        farm_data: Dict[str, Any],
        weather_forecast: List[Dict[str, Any]],
        historical_data: List[Dict[str, Any]] = None,
        days: int = 7,
    ) -> List[Dict[str, Any]]:
        """
        Returns list of {date, workers_needed, confidence}.

        Strategy:
        - Baseline: historical average for same crop/stage/season
        - Weather adjustment: rain reduces field work, clear skies boost it
        - Urgency adjustment: if harvest window is near, increase
        """
        # TODO: Load trained Prophet/XGBoost model for better accuracy
        today = datetime.date.today()
        crop_stage = farm_data.get("current_stage", "weeding")
        baseline = self.CROP_STAGE_BASELINE.get(crop_stage, 4)

        results = []
        for i, forecast in enumerate(weather_forecast[:days]):
            date = today + datetime.timedelta(days=i)
            workers = baseline
            confidence = 0.70

            # Weather adjustment
            rainfall = forecast.get("rainfall", 0)
            if rainfall > 5:
                # Heavy rain — reduce field work
                workers = max(1, int(workers * 0.5))
                confidence -= 0.10
            elif rainfall > 0:
                # Light rain — slight reduction
                workers = max(1, int(workers * 0.8))
                confidence -= 0.05

            results.append({
                "date": date.isoformat(),
                "workers_needed": workers,
                "confidence": round(max(0.4, confidence), 2),
            })

        return results
