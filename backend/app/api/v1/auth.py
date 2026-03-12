from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.dependencies import get_db, get_current_user
from app.services.auth_service import AuthService
from app.schemas.user import UserResponse
from app.models.user import User

router = APIRouter()
auth_service = AuthService()


class SendOTPRequest(BaseModel):
    phone: str


class VerifyOTPRequest(BaseModel):
    phone: str
    otp: str
    session_id: str


class RefreshTokenRequest(BaseModel):
    pass


@router.post("/send-otp")
async def send_otp(request: SendOTPRequest):
    """Send OTP to the given phone number."""
    session_id = await auth_service.send_otp(request.phone)
    return {"message": "OTP sent", "session_id": session_id}


@router.post("/verify-otp")
async def verify_otp(request: VerifyOTPRequest, db: AsyncSession = Depends(get_db)):
    """Verify OTP and return JWT access token with user profile."""
    await auth_service.verify_otp(request.phone, request.otp, request.session_id)

    result = await db.execute(select(User).where(User.phone == request.phone))
    user = result.scalar_one_or_none()

    if user is None:
        return {
            "access_token": None,
            "token_type": "bearer",
            "user": None,
            "message": "User not found. Please complete registration.",
        }

    token = auth_service.create_access_token(str(user.id))
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": UserResponse.model_validate(user),
    }


@router.post("/refresh-token")
async def refresh_token(current_user: User = Depends(get_current_user)):
    """Issue a new access token for the authenticated user."""
    token = auth_service.create_access_token(str(current_user.id))
    return {"access_token": token, "token_type": "bearer"}
