from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://assessment_user:assessment_pass@db:5432/assessment_db"
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    CORS_ORIGINS: str = "http://localhost:3000"
    OPENAI_API_KEY: str | None = None
    JUDGE0_BASE_URL: str | None = None
    JUDGE0_RAPIDAPI_KEY: str | None = None

settings = Settings()
