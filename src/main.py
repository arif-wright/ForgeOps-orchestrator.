"""ForgeOps CLI entrypoint."""

import logging

from src.config import get_settings
from src.logging_setup import configure_logging


def main() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)

    logger = logging.getLogger("forgeops")
    logger.info(
        "ForgeOps startup",
        extra={
            "environment": settings.env,
            "runner_name": settings.runner_name,
            "codex_model": settings.codex_model,
        },
    )


if __name__ == "__main__":
    main()
