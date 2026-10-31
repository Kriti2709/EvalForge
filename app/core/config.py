from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str = "EvalForge"

    VERSION: str = "0.1.0"

    ENVIRONMENT: str = "development"

    DATABASE_URL: str = "sqlite:///./evalforge.db"

    MONITORING_ENABLED: bool = True

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()