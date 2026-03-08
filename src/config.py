from __future__ import annotations

import os

from pydantic import BaseModel, ValidationError


class AppConfig(BaseModel):
    app_name: str = "forgeops"
    environment: str = "dev"
    log_level: str = "INFO"
    json_logs: bool = True


def _to_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


def load_config() -> AppConfig:
    raw = {
        "app_name": os.getenv("FORGEOPS_APP_NAME", "forgeops"),
        "environment": os.getenv("FORGEOPS_ENV", "dev"),
        "log_level": os.getenv("FORGEOPS_LOG_LEVEL", "INFO").upper(),
        "json_logs": _to_bool(os.getenv("FORGEOPS_JSON_LOGS"), True),
    }
    try:
        return AppConfig.model_validate(raw)
    except ValidationError as exc:
        raise SystemExit(f"Invalid configuration: {exc}") from exc
