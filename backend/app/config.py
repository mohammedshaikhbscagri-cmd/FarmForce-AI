from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/farmforce"
    REDIS_URL: str = "redis://localhost:6379"
    RAZORPAY_KEY_ID: str = ""
    RAZORPAY_KEY_SECRET: str = ""
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE: str = ""
    TOMORROW_IO_API_KEY: str = ""
    JWT_SECRET_KEY: str = "changeme-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 1440
    FIREBASE_CONFIG_PATH: str = ""
    PLATFORM_COMMISSION_RATE: float = 0.075
    APP_NAME: str = "FarmForce AI"
    DEBUG: bool = False

    @model_validator(mode="after")
    def validate_production_secrets(self) -> "Settings":
        if not self.DEBUG and self.JWT_SECRET_KEY == "changeme-in-production":
            raise ValueError(
                "JWT_SECRET_KEY must be changed from the default value in production (DEBUG=False)"
            )
        return self

    class Config:
        env_file = ".env"


settings = Settings()
