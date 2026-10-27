
from fastapi import FastAPI

import app
from app.core.lifespan import lifespan
from app.core.middleware import RequestLoggingMiddleware
from app.exceptions.exception_handlers import  app_exception_handler, unexpected_exception_handler
from app.exceptions.exceptions_log import NotFoundException
from app.routes import api_router
from app.core.config import settings


def create_app():
    app = FastAPI(
        title= settings.app_name,
        version= settings.app_version,
        debug= settings.debug,
        docs_url= "/docs",
        redoc_url= "/redoc",
        openapi_url= "/openapi.json",
        lifespan=lifespan
    )

    # # 1. Register exception handlers
    # app.add_exception_handler(NotFoundException, app_exception_handler)
    # app.add_exception_handler(Exception, unexpected_exception_handler)

    # 2. Register middleware
    app.add_middleware(RequestLoggingMiddleware)

    # 3. Include routers
    app.include_router(api_router)

    return app