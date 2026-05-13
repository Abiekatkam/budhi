from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME: str = "BUDHI"
    ENVIRONMENT: str = "development"

    DATABASE_URL: str

    REDIS_URL: str

    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    OLLAMA_BASE_URL: str

    EMBEDDING_MODEL: str
    LLM_MODEL: str

    class Config:
        env_file = "../.env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()