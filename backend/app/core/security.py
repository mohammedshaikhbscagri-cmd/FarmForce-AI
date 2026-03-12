import hashlib
from datetime import datetime, timedelta
from jose import jwt, JWTError

from app.config import settings


def create_access_token(data: dict) -> str:
    """Create a signed JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def verify_access_token(token: str) -> dict:
    """Verify and decode a JWT token. Raises JWTError on failure."""
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])


def hash_aadhaar(aadhaar: str) -> str:
    """Return SHA-256 hex digest of an Aadhaar number."""
    return hashlib.sha256(aadhaar.encode()).hexdigest()
