"""
Data loading and preprocessing utilities for the prediction pipeline.
"""
import pandas as pd
from typing import List, Dict, Any, Optional


def load_historical_bookings(filepath: str) -> pd.DataFrame:
    """Load historical booking data from CSV."""
    # TODO: Load from actual data source (database or S3)
    df = pd.read_csv(filepath)
    df["created_at"] = pd.to_datetime(df["created_at"])
    return df


def load_weather_data(filepath: str) -> pd.DataFrame:
    """Load historical weather data."""
    df = pd.read_csv(filepath)
    df["date"] = pd.to_datetime(df["date"])
    return df


def compute_rolling_averages(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    """Compute rolling averages for labor demand."""
    df = df.copy()
    df = df.sort_values("date")
    df["workers_rolling_avg"] = df["workers_needed"].rolling(window=window, min_periods=1).mean()
    return df


def aggregate_by_district_task(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate wages and demand by district + task type."""
    return df.groupby(["district", "task_type"]).agg(
        avg_wage=("wage_per_day", "mean"),
        median_wage=("wage_per_day", "median"),
        max_wage=("wage_per_day", "max"),
        min_wage=("wage_per_day", "min"),
        total_jobs=("id", "count"),
    ).reset_index()


def preprocess_for_model(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess data for ML model training."""
    df = df.copy()
    df["month"] = df["date"].dt.month
    df["day_of_week"] = df["date"].dt.dayofweek
    df["is_kharif_season"] = df["month"].isin([6, 7, 8, 9, 10])
    df["is_rabi_season"] = df["month"].isin([11, 12, 1, 2, 3])
    return df
