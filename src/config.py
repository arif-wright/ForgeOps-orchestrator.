"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Strongly typed runtime settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    env: str = Field(default="development", alias="FORGEOPS_ENV")
    log_level: str = Field(default="INFO", alias="FORGEOPS_LOG_LEVEL")
    runner_name: str = Field(
        default="github-self-hosted-runner",
        alias="FORGEOPS_RUNNER_NAME",
    )
    codex_model: str = Field(default="gpt-5-codex", alias="FORGEOPS_CODEX_MODEL")
    max_concurrent_runs: int = Field(default=2, alias="FORGEOPS_MAX_CONCURRENT_RUNS")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()
