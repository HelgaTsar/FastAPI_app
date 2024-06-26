from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:123456@localhost:5432//hw-12"
    SECRET_KEY_JWT: str = "1234567890"
    ALGORITHM: str = "HS256"
    MAIL_USERNAME: EmailStr = "helgats@meta.ua"
    MAIL_PASSWORD: str = "e3B53943"
    MAIL_FROM: str = "helgats@meta.ua"
    MAIL_PORT: int = 567234
    MAIL_SERVER: str = "smtp.meta.ua"
    REDIS_DOMAIN: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    CLD_NAME: str = 'hw-12'
    CLD_API_KEY: int = 645381621127547
    CLD_API_SECRET: str = 'secret'

    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, v: Any):
        if v not in ["HS256", "HS512"]:
            raise ValueError("algorithm must be HS256 or HS512")
        return v


    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Settings()