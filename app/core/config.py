
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    DATABASE_URL: str = Field(..., validation_alias="DATABASE_URL")
    JWT_SECRET: str = Field(..., validation_alias="JWT_SECRET")
    JWT_ALG: str = Field(default="HS256", validation_alias="JWT_ALG")
    JWT_EXPIRES_MIN: int = Field(default=60*24, validation_alias="JWT_EXPIRES_MIN")
    PROJECT_NAME: str = "devinote"

settings = Settings()
