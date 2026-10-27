
from fastapi import APIRouter
from app.routes.health_check_router import router as health_check_router
from app.routes.source import router as source_router
from app.routes.article import router as article_router

api_router = APIRouter()
api_router.include_router(health_check_router)
api_router.include_router(source_router)
api_router.include_router(article_router)
