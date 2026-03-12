# FarmForce AI — API Specification

Base URL: `http://localhost:8000/api/v1`

All authenticated endpoints require: `Authorization: Bearer <JWT_TOKEN>`

---

## Auth

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /auth/send-otp | No | Send OTP to phone |
| POST | /auth/verify-otp | No | Verify OTP, get JWT |
| POST | /auth/refresh-token | Yes | Get new access token |

### POST /auth/send-otp
```json
Request: { "phone": "+919876543210" }
Response: { "message": "OTP sent", "session_id": "uuid" }
```

### POST /auth/verify-otp
```json
Request: { "phone": "+91...", "otp": "123456", "session_id": "uuid" }
Response: { "access_token": "jwt...", "token_type": "bearer", "user": {...} }
```

---

## Users

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /users/me | Yes | Get current user profile |
| PUT | /users/me | Yes | Update profile |
| GET | /users/{user_id} | No | Get public profile |
| POST | /users/me/farm | Yes (Farmer) | Add farm |
| PUT | /users/me/skills | Yes (Worker) | Update skills |

---

## Jobs

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /jobs | Yes (Farmer) | Create job |
| GET | /jobs | No | List open jobs (with filters) |
| GET | /jobs/my-jobs | Yes (Farmer) | My posted jobs |
| GET | /jobs/{job_id} | No | Job details |
| PUT | /jobs/{job_id} | Yes (Owner) | Update job |
| DELETE | /jobs/{job_id} | Yes (Owner) | Cancel job |
| POST | /jobs/voice | Yes (Farmer) | Create job from voice |

### GET /jobs Query Parameters
- `task_type`: TaskType enum
- `min_wage`: minimum wage per day
- `district`: filter by district
- `latitude`, `longitude`, `max_distance_km`: geo filter

---

## Bookings

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /bookings | Yes (Worker) | Apply for job |
| GET | /bookings | Yes | My bookings |
| PUT | /bookings/{id}/check-in | Yes (Worker) | GPS check-in |
| PUT | /bookings/{id}/check-out | Yes (Worker) | Check-out |
| PUT | /bookings/{id}/confirm | Yes (Farmer) | Confirm work done |
| PUT | /bookings/{id}/cancel | Yes | Cancel booking |

---

## Payments

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /payments/create-order | Yes (Farmer) | Create Razorpay order |
| POST | /payments/verify | No | Verify payment signature |
| POST | /payments/{id}/release | Yes | Release escrow to worker |
| GET | /payments/history | Yes | Payment history |

---

## Matching

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /matching/workers?job_id= | No | Ranked workers for job |
| GET | /matching/jobs?worker_id= | No | Ranked jobs for worker |

---

## Predictions

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | /predictions/labor-demand?farm_id= | No | 7-day labor forecast |
| GET | /predictions/wage-suggestion?task_type=&district= | No | Wage suggestion |

---

## Health

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
