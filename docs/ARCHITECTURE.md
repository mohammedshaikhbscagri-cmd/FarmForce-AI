# FarmForce AI — System Architecture

## Overview

FarmForce AI follows a **layered microservice-ready monolith** architecture designed for the Indian market, with progressive enhancement toward distributed services as scale demands.

## Component Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                                │
│  ┌──────────────────────┐          ┌────────────────────────────┐  │
│  │   Flutter Mobile App  │          │   React Admin Dashboard    │  │
│  │  (Android + iOS)      │          │   (Web Browser)            │  │
│  └──────────┬───────────┘          └──────────────┬─────────────┘  │
└─────────────┼────────────────────────────────────┼─────────────────┘
              │ HTTPS REST + JWT                    │ HTTPS REST
┌─────────────▼────────────────────────────────────▼─────────────────┐
│                         API LAYER                                   │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │              FastAPI Backend (Python 3.11)                     │ │
│  │  /auth  /users  /jobs  /bookings  /payments  /matching  /ai   │ │
│  └───────────────────────────────────────────────────────────────┘ │
└────────────┬───────────┬────────────┬───────────┬──────────────────┘
             │           │            │           │
┌────────────▼──┐ ┌──────▼───┐ ┌─────▼────┐ ┌───▼────────────────┐
│  PostgreSQL   │ │  Redis   │ │ Razorpay │ │ Firebase + Twilio  │
│  (PostGIS)   │ │  Cache   │ │ Payments │ │ (Auth + Push + SMS)│
└───────────────┘ └──────────┘ └──────────┘ └────────────────────┘
```

## Data Flow

### Job Posting Flow
1. Farmer opens app → POST /api/v1/jobs
2. Backend creates job record (status=OPEN)
3. Matching engine indexes nearby workers
4. Push notifications sent to matched workers via FCM

### Payment Escrow Flow
1. Farmer creates payment order → POST /payments/create-order
2. Razorpay order created → farmer completes UPI payment
3. POST /payments/verify → payment held in escrow (HELD_IN_ESCROW)
4. Worker checks in (GPS geofence verified)
5. Farmer confirms work → POST /bookings/{id}/confirm
6. POST /payments/{id}/release → Razorpay Route transfer to worker UPI
7. 7.5% commission retained by platform

## Tech Stack Justification

| Choice | Reason |
|--------|--------|
| FastAPI | Async-native, high performance, auto-generated OpenAPI docs |
| PostgreSQL + PostGIS | ACID transactions + spatial indexing for geo queries |
| Redis | Session storage, job feed caching, rate limiting |
| Flutter | Single codebase for Android + iOS, offline support |
| Riverpod | Compile-safe state management in Flutter |
| Razorpay | Best UPI support in India, Route API for disbursements |
| Firebase | Phone OTP auth + FCM push notifications |
| Twilio | SMS + WhatsApp fallback for low-connectivity areas |

## Deployment Architecture (AWS ap-south-1 Mumbai)

```
Internet → AWS ALB → EC2 t3.small (FastAPI)
                  ↓
         RDS db.t3.micro (PostgreSQL 16)
         ElastiCache cache.t3.micro (Redis 7)
         S3 (Media storage)
```
