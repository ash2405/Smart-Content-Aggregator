
from fastapi import APIRouter
from app.routes.health_check_router import router as health_check_router
from app.routes.source import router as source_router
from app.routes.article import router as article_router
from app.routes.article_file import router as article_file_router
from app.routes.external_api import router as external_api

api_router = APIRouter()
api_router.include_router(health_check_router)
api_router.include_router(source_router)
api_router.include_router(article_router)
api_router.include_router(article_file_router)
api_router.include_router(external_api)
