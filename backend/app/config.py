from pydantic_settings import BaseSettings


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

    class Config:
        env_file = ".env"


settings = Settings()
