from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    project_name: str = "ResearchOS"
    environment: str = "development"
    mistral_api_key: str
    model_name: str = "mistral-small-latest"
    temperature: float = 0.0
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

@ lru_cache
def get_settings():
    return Settings()