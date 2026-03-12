# 🚜 FarmForce AI

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flutter](https://img.shields.io/badge/Flutter-3.16-blue?logo=flutter)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

> **"Har Kisan ko Mazdoor, Har Mazdoor ko Kaam"**
> *(Every farmer finds workers, every worker finds jobs)*

**FarmForce AI** is an AI-powered, two-sided mobile marketplace connecting Indian farmers with verified farm workers. Built with voice-first UX, offline support, and UPI payments to serve India's 14.6 crore farming households.

---

## 🌾 The Problem

India's agricultural sector faces a critical labor crisis:

| Stat | Number |
|------|--------|
| Total farmers | 14.6 Crore |
| Small & marginal farmers | 86% |
| Annual farmer suicides | 10,786/year |
| Daily wage range | ₹300–₹700/day |
| Seasonal labor shortage | 30-40% of harvest lost |
| Workers without digital access | 70%+ |

Farmers spend 2–4 days finding labor during critical harvest windows, losing crops and money. Workers travel blindly to find work, often settling for below-market wages.

---

## ✅ The Solution

FarmForce AI digitizes the farm labor marketplace with:

- 🤖 **AI Matching**: ML-powered worker-job matching based on skill, distance, rating, reliability
- 🎤 **Voice First**: Post jobs and find work in Hindi, Marathi, Gujarati, Tamil, Telugu + 5 more
- 📴 **Offline Ready**: Works without internet; syncs when connected
- 💳 **UPI Payments**: Secure escrow + instant UPI transfer via Razorpay Route
- 🚁 **Drone/Tractor**: Backup labor from drone spray & equipment services
- 🌦️ **Weather AI**: Labor demand forecasting using crop stage + weather data

---

## 🚀 Key Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Worker Matching | Weighted scoring: distance (35%), skills (30%), rating (20%), reliability (15%) |
| 🎤 Voice Job Posting | Whisper ASR + NLU for Hindi/Marathi job posting |
| 💰 Dynamic Pricing | Fair wage suggestions based on season, district, supply/demand |
| 📍 GPS Check-in | 100-meter geofence check-in for attendance |
| 💳 Escrow Payments | Farmer pays → Escrow → Auto-release after work confirmation |
| 🔔 Smart Alerts | Push + SMS + WhatsApp notifications via Firebase + Twilio |
| 📊 Admin Dashboard | React dashboard with real-time analytics and dispute management |
| 🌐 Multi-language | 9 Indian languages with Flutter localization |

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend API** | FastAPI 0.109 + Python 3.11 |
| **Database** | PostgreSQL 16 + PostGIS (spatial queries) |
| **Cache** | Redis 7 |
| **Mobile App** | Flutter 3.16 + Dart |
| **State Management** | Riverpod 2.4 |
| **Payments** | Razorpay + Razorpay Route (escrow) |
| **Authentication** | Firebase Phone Auth + JWT |
| **SMS/WhatsApp** | Twilio |
| **AI Matching** | Custom weighted scoring + scikit-learn |
| **Voice** | OpenAI Whisper + custom NLU |
| **Demand Forecast** | Prophet + XGBoost |
| **Weather** | Tomorrow.io API |
| **Admin** | React 18 + Tailwind CSS + Recharts |
| **Infrastructure** | AWS (EC2, RDS, ElastiCache, S3) |
| **CI/CD** | GitHub Actions |
| **Containerization** | Docker + Docker Compose |
| **IaC** | Terraform |

---

## 🏛️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Flutter Mobile App                    │
│        (Farmer App)         (Worker App)                 │
│  Post Job | Pay | Track    Search | Apply | Check-in    │
└────────────────────┬────────────────────────────────────┘
                     │ HTTPS / REST API
┌────────────────────▼────────────────────────────────────┐
│                   FastAPI Backend                        │
│  Auth | Jobs | Bookings | Payments | Matching | AI       │
└──┬──────────┬───────────┬──────────┬──────────┬─────────┘
   │          │           │          │          │
   ▼          ▼           ▼          ▼          ▼
PostgreSQL  Redis     Razorpay   Firebase   Tomorrow.io
(PostGIS)  (Cache)   (Payments)  (Auth+FCM)  (Weather)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Flutter 3.16+
- Docker & Docker Compose
- Node.js 18+ (for admin dashboard)
- PostgreSQL 16 (or use Docker)

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials

# Run database migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload
```

### Mobile Setup

```bash
cd mobile
flutter pub get
flutter run
```

### Admin Dashboard Setup

```bash
cd admin
npm install
npm run dev
```

### Docker Setup (All Services)

```bash
cd infra
docker-compose up -d
```

---

## 📁 Project Structure

```
FarmForce-AI/
├── backend/                    # FastAPI Python backend
│   ├── app/
│   │   ├── main.py             # FastAPI app + CORS + routers
│   │   ├── config.py           # Pydantic settings
│   │   ├── database.py         # SQLAlchemy async engine
│   │   ├── models/             # SQLAlchemy ORM models
│   │   ├── schemas/            # Pydantic v2 schemas
│   │   ├── api/v1/             # REST API endpoints
│   │   ├── services/           # Business logic
│   │   ├── core/               # Security, dependencies, exceptions
│   │   └── utils/              # Geo, SMS, constants
│   ├── alembic/                # DB migrations
│   ├── tests/                  # pytest test suite
│   └── requirements.txt
├── mobile/                     # Flutter mobile app
│   ├── lib/
│   │   ├── app/                # Routes, theme, app.dart
│   │   ├── config/             # API config, constants
│   │   ├── models/             # Dart model classes
│   │   ├── services/           # API, Auth, Location, Payment...
│   │   ├── providers/          # Riverpod state management
│   │   ├── screens/            # All UI screens
│   │   ├── widgets/            # Reusable widgets
│   │   └── l10n/               # i18n (en, hi, mr)
│   └── pubspec.yaml
├── ai_ml/                      # AI/ML modules
│   ├── matching/               # Worker-job matching engine
│   ├── prediction/             # Labor demand prediction
│   ├── pricing/                # Dynamic wage pricing
│   ├── voice/                  # Voice-to-job parser
│   └── notebooks/              # Jupyter notebooks
├── admin/                      # React admin dashboard
│   └── src/
│       ├── pages/              # Dashboard, Users, Jobs, Transactions, Disputes
│       └── components/         # Sidebar, StatsCard, DataTable
├── infra/                      # Infrastructure
│   ├── docker-compose.yml
│   ├── terraform/              # AWS IaC
│   └── .github/workflows/      # CI/CD pipelines
└── docs/                       # Documentation
    ├── PRD.md
    ├── ARCHITECTURE.md
    ├── API_SPEC.md
    ├── DATABASE_SCHEMA.md
    ├── DEPLOYMENT.md
    └── CONTRIBUTING.md
```

---

## 📖 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

See [docs/API_SPEC.md](docs/API_SPEC.md) for full API documentation.

---

## 🤝 Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for contribution guidelines.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Built for India's farming community — dedicated to the 14.6 crore farmers and 90+ crore agricultural workers who feed our nation.
