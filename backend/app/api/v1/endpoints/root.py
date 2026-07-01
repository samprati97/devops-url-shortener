import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
def read_root(settings: Annotated[Settings, Depends(get_settings)]) -> dict[str, str]:
    """Root endpoint — confirms the API is running."""
    logger.info("Root endpoint called")
    return {
        "service": settings.app_name,
        "environment": settings.app_env,
        "status": "running",
    }
