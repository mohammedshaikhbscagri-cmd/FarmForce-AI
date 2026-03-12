# FarmForce AI — Product Requirements Document (PRD)

## Overview
FarmForce AI connects Indian farmers with farm workers through an AI-powered marketplace.

## Requirements

### F1 — Authentication
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| F1.1 | OTP-based phone login | P0 | Firebase Phone Auth, 6-digit OTP |
| F1.2 | JWT session management | P0 | 24-hour tokens, refresh supported |
| F1.3 | Role selection | P0 | Farmer / Worker / Contractor |

### F2 — Farmer Features
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| F2.1 | Post job with task type, wage, date, location | P0 | All required fields |
| F2.2 | Voice job posting | P1 | Whisper ASR + Hindi NLU |
| F2.3 | View AI-matched workers | P0 | Ranked by composite score |
| F2.4 | Confirm/reject applications | P0 | Push notification to worker |
| F2.5 | GPS-verified attendance | P1 | Geofence check-in/out |
| F2.6 | Escrow payment release | P0 | After work confirmation |
| F2.7 | Rate and review workers | P1 | 1-5 stars + comment |

### F3 — Worker Features
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| W1.1 | Search jobs by location/task/wage | P0 | Filters + sort |
| W1.2 | Apply for jobs | P0 | One-tap application |
| W1.3 | GPS check-in at farm | P0 | 100m geofence |
| W1.4 | View earnings history | P1 | UPI transfer records |
| W1.5 | Skill badges | P2 | Bronze/Silver/Gold verification |

### F4 — Matching Engine
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| M1.1 | Distance score | P0 | 35% weight, max 50km |
| M1.2 | Skill match score | P0 | 30% weight |
| M1.3 | Rating score | P0 | 20% weight |
| M1.4 | Reliability score | P0 | 15% weight |

### F5 — Payments
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| P1.1 | Razorpay UPI payment | P0 | INR, paise conversion |
| P1.2 | Escrow hold | P0 | HELD_IN_ESCROW status |
| P1.3 | Auto-release on confirmation | P0 | 7.5% platform commission |
| P1.4 | Worker UPI transfer | P0 | Razorpay Route API |

### F6 — AI/ML Features
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| AI1.1 | Labor demand forecasting | P1 | 7-day forecast |
| AI1.2 | Dynamic wage pricing | P1 | Supply/demand + season |
| AI1.3 | Voice NLU (Hindi/Marathi) | P1 | Whisper + entity extraction |

### F7 — Admin Features
| Req ID | Description | Priority | Details |
|--------|-------------|----------|---------|
| A1.1 | User management | P0 | View, verify, suspend |
| A1.2 | Job management | P0 | View, cancel, moderate |
| A1.3 | Transaction monitoring | P0 | Real-time payment status |
| A1.4 | Dispute resolution | P1 | Assign, resolve, close |
| A1.5 | Analytics dashboard | P1 | GMV, users, jobs, revenue |
| A1.6 | Farmer verification | P1 | Aadhaar hash verification |
| A1.7 | Worker skill verification | P2 | Badge assignment |
| A1.8 | Outbreak warnings | P2 | Push broadcast notifications |
