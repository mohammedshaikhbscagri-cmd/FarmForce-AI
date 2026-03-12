# FarmForce AI — Database Schema

## Tables

### users
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK, default uuid4 | User ID |
| phone | VARCHAR(15) | UNIQUE, NOT NULL | Phone number |
| role | ENUM | NOT NULL | farmer/worker/contractor |
| name | VARCHAR(255) | NULLABLE | Full name |
| village | VARCHAR(255) | NULLABLE | Village name |
| district | VARCHAR(255) | NULLABLE | District |
| state | VARCHAR(255) | NULLABLE | State |
| language_pref | VARCHAR(10) | DEFAULT 'hi' | Preferred language |
| aadhaar_hash | VARCHAR(64) | NULLABLE | SHA-256 of Aadhaar |
| upi_id | VARCHAR(255) | NULLABLE | UPI ID for payments |
| avg_rating | FLOAT | DEFAULT 0.0 | Average rating |
| total_jobs | INTEGER | DEFAULT 0 | Jobs completed |
| is_verified | BOOLEAN | DEFAULT FALSE | KYC verified |
| is_active | BOOLEAN | DEFAULT TRUE | Account active |
| created_at | DATETIME | server_default=now | Created timestamp |
| updated_at | DATETIME | onupdate=now | Updated timestamp |

### jobs
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Job ID |
| farmer_id | UUID | FK→users | Farmer who posted |
| task_type | ENUM | NOT NULL | Agricultural task |
| crop_type | VARCHAR(255) | NOT NULL | Crop name |
| workers_needed | INTEGER | NOT NULL | Number of workers |
| wage_per_day | NUMERIC(10,2) | NOT NULL | Daily wage in INR |
| start_date | DATE | NOT NULL | Work start date |
| end_date | DATE | NOT NULL | Work end date |
| location_lat | FLOAT | NOT NULL | GPS latitude |
| location_lng | FLOAT | NOT NULL | GPS longitude |
| village | VARCHAR(255) | NOT NULL | Village |
| district | VARCHAR(255) | NOT NULL | District |
| state | VARCHAR(255) | NOT NULL | State |
| status | ENUM | DEFAULT OPEN | Job status |
| urgency | ENUM | DEFAULT NORMAL | Normal/Urgent |
| description | TEXT | NULLABLE | Job description |

### bookings
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Booking ID |
| job_id | UUID | FK→jobs | Job reference |
| worker_id | UUID | FK→users | Worker reference |
| status | ENUM | DEFAULT PENDING | Booking status |
| check_in_time | DATETIME | NULLABLE | GPS check-in time |
| check_out_time | DATETIME | NULLABLE | Check-out time |
| check_in_lat | FLOAT | NULLABLE | Check-in latitude |
| check_in_lng | FLOAT | NULLABLE | Check-in longitude |
| farmer_confirmed | BOOLEAN | DEFAULT FALSE | Work confirmed |

### payments
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | PK | Payment ID |
| booking_id | UUID | FK→bookings | Booking reference |
| farmer_id | UUID | FK→users | Payer |
| worker_id | UUID | FK→users | Recipient |
| amount | NUMERIC(10,2) | NOT NULL | Total amount |
| platform_commission | NUMERIC(10,2) | NOT NULL | 7.5% commission |
| worker_payout | NUMERIC(10,2) | NOT NULL | Worker receives |
| status | ENUM | DEFAULT PENDING | Payment status |
| razorpay_order_id | VARCHAR | NULLABLE | Razorpay order |
| razorpay_payment_id | VARCHAR | NULLABLE | Razorpay payment |
| razorpay_transfer_id | VARCHAR | NULLABLE | Razorpay transfer |
| payment_mode | ENUM | DEFAULT UPI | UPI/CASH/WALLET |

## Relationships

```
users ─── jobs (farmer_id)
users ─── bookings (worker_id)
users ─── worker_skills (worker_id)
users ─── farmer_farms (farmer_id)
jobs ─── bookings (job_id)
bookings ─── payments (booking_id)
bookings ─── reviews (booking_id)
```

## Indexes (Recommended)

```sql
CREATE INDEX idx_jobs_district ON jobs(district);
CREATE INDEX idx_jobs_status ON jobs(status);
CREATE INDEX idx_jobs_location ON jobs USING GIST(ST_MakePoint(location_lng, location_lat));
CREATE INDEX idx_bookings_worker ON bookings(worker_id);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_payments_status ON payments(status);
```
