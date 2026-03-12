"""
Dynamic pricing engine to suggest fair wages based on supply/demand.
"""
import datetime
from typing import Dict, Any


class DynamicPricingEngine:
    """Calculate fair wage suggestions based on supply/demand, season, and location."""

    # Regional baseline daily wages (INR) by task type
    BASELINE_WAGES = {
        "HARVESTING": 450,
        "WEEDING": 300,
        "SOWING": 350,
        "TRANSPLANTING": 380,
        "SPRAYING": 400,
        "THRESHING": 400,
        "LOADING": 350,
        "PRUNING": 380,
        "IRRIGATION": 320,
        "OTHER": 300,
    }

    # Seasonal multipliers for Kharif (Jun-Oct) and Rabi (Nov-Mar)
    SEASON_MULTIPLIERS = {
        "kharif": 1.15,  # Higher demand during Kharif harvest
        "rabi": 1.10,
        "off": 1.00,
    }

    def _get_season(self, date: datetime.date) -> str:
        month = date.month
        if 6 <= month <= 10:
            return "kharif"
        elif month in [11, 12, 1, 2, 3]:
            return "rabi"
        return "off"

    def suggest_wage(
        self,
        task_type: str,
        district: str,
        date: datetime.date = None,
        supply_level: str = "medium",
        demand_level: str = "medium",
    ) -> Dict[str, Any]:
        """
        Returns {min_wage, max_wage, suggested_wage, supply_level, demand_level}.

        Args:
            task_type: Type of agricultural task.
            district: Indian district name.
            date: Date for which to calculate (defaults to today).
            supply_level: 'low' | 'medium' | 'high' (worker availability).
            demand_level: 'low' | 'medium' | 'high' (farmer demand).
        """
        if date is None:
            date = datetime.date.today()

        base = self.BASELINE_WAGES.get(task_type.upper(), 300)
        season = self._get_season(date)
        season_mult = self.SEASON_MULTIPLIERS[season]

        # Supply-demand adjustment
        demand_map = {"low": 0.85, "medium": 1.00, "high": 1.20}
        supply_map = {"low": 1.15, "medium": 1.00, "high": 0.85}
        adjustment = demand_map.get(demand_level, 1.0) * supply_map.get(supply_level, 1.0)

        # TODO: Apply district-level wage index from historical data
        # district_multiplier = get_district_wage_index(district)

        suggested = int(base * season_mult * adjustment)
        return {
            "task_type": task_type,
            "district": district,
            "date": date.isoformat(),
            "min_wage": int(suggested * 0.85),
            "max_wage": int(suggested * 1.20),
            "suggested_wage": suggested,
            "supply_level": supply_level,
            "demand_level": demand_level,
            "season": season,
        }
