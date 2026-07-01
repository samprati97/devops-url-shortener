import logging
import sys

from app.core.config import Settings


def setup_logging(settings: Settings) -> None:
    """Configure structured logging for the application."""
    log_format = (
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
        if settings.is_production
        else "%(levelname)-8s | %(name)s | %(message)s"
    )

    logging.basicConfig(
        level=settings.log_level.upper(),
        format=log_format,
        stream=sys.stdout,
        force=True,
    )

    # Reduce noise from third-party libraries in production
    if settings.is_production:
        logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
