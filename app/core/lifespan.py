from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.loging import setup_logging
from loguru import logger

from app.core.config import settings

@asynccontextmanager
async def lifespan(app: "FastAPI"):
    setup_logging()

    logger.info("Starting the application...")
    yield
    logger.info("Shutting down the application...")
