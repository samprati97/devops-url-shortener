from fastapi import APIRouter

from app.api.v1.endpoints import root

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(root.router, tags=["root"])
