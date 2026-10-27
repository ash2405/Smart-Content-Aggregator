
from fastapi import APIRouter
from app.routes.health_check_router import router as health_check_router

api_router = APIRouter()
api_router.include_router(health_check_router)

