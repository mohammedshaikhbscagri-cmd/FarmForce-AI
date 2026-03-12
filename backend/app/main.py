from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.v1 import auth, users, jobs, bookings, payments, reviews, matching, services, predictions
from app.core.exceptions import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("FarmForce AI backend starting up...")
    yield
    # Shutdown
    print("FarmForce AI backend shutting down...")


app = FastAPI(
    title="FarmForce AI API",
    description="AI-Powered Farm Labor Marketplace for India",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

API_PREFIX = "/api/v1"

app.include_router(auth.router, prefix=API_PREFIX + "/auth", tags=["auth"])
app.include_router(users.router, prefix=API_PREFIX + "/users", tags=["users"])
app.include_router(jobs.router, prefix=API_PREFIX + "/jobs", tags=["jobs"])
app.include_router(bookings.router, prefix=API_PREFIX + "/bookings", tags=["bookings"])
app.include_router(payments.router, prefix=API_PREFIX + "/payments", tags=["payments"])
app.include_router(reviews.router, prefix=API_PREFIX + "/reviews", tags=["reviews"])
app.include_router(matching.router, prefix=API_PREFIX + "/matching", tags=["matching"])
app.include_router(services.router, prefix=API_PREFIX + "/services", tags=["services"])
app.include_router(predictions.router, prefix=API_PREFIX + "/predictions", tags=["predictions"])


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy", "app": "FarmForce AI"}
