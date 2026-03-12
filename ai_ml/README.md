# FarmForce AI — AI/ML Module

This module contains all machine learning and AI components for the FarmForce AI platform.

## Modules

### 🎯 Matching Engine (`matching/`)
AI-powered worker-job matching using a weighted composite score:
- **Distance** (35%): Closer workers score higher
- **Skill Match** (30%): Exact skill match = 100 pts, related = 50 pts
- **Rating** (20%): Based on average user rating
- **Reliability** (15%): Completed jobs / total bookings ratio

### 📊 Demand Prediction (`prediction/`)
Predicts labor demand for farms using:
- Crop stage analysis
- Weather forecast integration (Tomorrow.io)
- Historical booking patterns
- **Planned**: Facebook Prophet + XGBoost ensemble model

### 💰 Dynamic Pricing (`pricing/`)
Fair wage suggestions based on:
- Regional baseline wages (Indian labor market data)
- Seasonal multipliers (Kharif/Rabi seasons)
- Supply-demand adjustments
- District-level wage indices

### 🎤 Voice Processing (`voice/`)
Voice-to-job conversion pipeline:
- **Step 1**: OpenAI Whisper transcription (Hindi/Marathi/Gujarati/...)
- **Step 2**: NLU entity extraction (task, workers, wage, crop)
- **Step 3**: Structured job data output

## Setup

```bash
cd ai_ml
pip install -r requirements.txt
```

## Training

```bash
# Run Jupyter notebooks for model development
jupyter notebook notebooks/
```

## Usage

```python
from matching.matching_model import MatchingEngine
from prediction.demand_predictor import LaborDemandPredictor
from pricing.dynamic_pricing import DynamicPricingEngine

# Match workers for a job
engine = MatchingEngine()
ranked = engine.rank_workers(workers, job)

# Predict demand
predictor = LaborDemandPredictor()
forecast = predictor.predict(farm_data, weather_forecast)

# Suggest wage
pricing = DynamicPricingEngine()
wage = pricing.suggest_wage("HARVESTING", "Pune")
```
