import uuid
from datetime import datetime

from app.core.security import create_access_token


class AuthService:
    """Handles OTP-based authentication and JWT token generation."""

    async def send_otp(self, phone: str) -> str:
        """Send OTP to the given phone number and return a session_id."""
        # TODO: Integrate Firebase Phone Auth or Twilio Verify for real OTP delivery
        session_id = str(uuid.uuid4())
        print(f"[AuthService] OTP sent to {phone} | session_id={session_id}")
        return session_id

    async def verify_otp(self, phone: str, otp: str, session_id: str):
        """Verify OTP and return (user_data, access_token). Raises on failure."""
        # TODO: Verify OTP against Firebase or Twilio session
        # Placeholder: accept any 6-digit OTP for demo purposes
        if len(otp) != 6 or not otp.isdigit():
            raise ValueError("Invalid OTP format")
        return phone

    def create_access_token(self, user_id: str) -> str:
        """Generate a signed JWT for the given user ID."""
        return create_access_token({"sub": str(user_id)})
