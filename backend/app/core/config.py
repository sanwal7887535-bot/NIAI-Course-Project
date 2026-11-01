from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", "../.env"), extra="ignore")

    # --- Core ---
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/shortlisting"
    REDIS_URL: str = "redis://localhost:6379/0"
    SECRET_KEY: str = "dev-only-change-me"  # production mein .env se zaroor badlein
    CORS_ORIGINS: str = "http://localhost:5173"  # comma separated

    # --- Intake & Matching (Member 1) ---
    SHORTLIST_THRESHOLD: int = 65
    CONSENT_NOTICE_VERSION: str = "v1"
    ANTHROPIC_API_KEY: str = ""
    LLM_MODEL: str = "claude-sonnet-5-5"


settings = Settings()
