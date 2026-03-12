# FarmForce AI — Deployment Guide

## Prerequisites

- AWS account with IAM permissions
- Docker + Docker Compose installed
- Terraform >= 1.6
- Domain name (optional)

## Environment Variables

Copy `backend/.env.example` to `backend/.env` and fill in all values:

```bash
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/farmforce
REDIS_URL=redis://host:6379
RAZORPAY_KEY_ID=rzp_live_...
RAZORPAY_KEY_SECRET=...
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
JWT_SECRET_KEY=<strong-random-secret>
FIREBASE_CONFIG_PATH=/etc/farmforce/firebase.json
```

## Local Docker Deployment

```bash
cd infra
docker-compose up -d

# Check logs
docker-compose logs -f backend
```

## AWS Deployment (Terraform)

```bash
cd infra/terraform

# Initialize
terraform init

# Plan
terraform plan -var="db_password=secure_pass" -var="key_pair_name=my-key"

# Apply
terraform apply -var="db_password=secure_pass" -var="key_pair_name=my-key"
```

## Database Migrations

```bash
cd backend
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "description"
```

## Monitoring

- **Logs**: CloudWatch Logs (configure in backend Docker CMD)
- **Metrics**: CloudWatch Metrics
- **Uptime**: AWS Route53 health checks

## Backup Strategy

- RDS: Automated daily snapshots (7-day retention)
- Redis: Persistence enabled (AOF)
- S3: Versioning enabled on media bucket
