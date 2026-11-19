from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.loging import setup_logging
from loguru import logger

from app.core.config import settings
from app.core.redis import check_redis_connection , redis_client

@asynccontextmanager
async def lifespan(app: "FastAPI"):

    await check_redis_connection()
    yield


    await redis_client.aclose()
    print("Redis connection closed successfully!")

    setup_logging()
    logger.info("Starting the application...")
    yield
    logger.info("Shutting down the application...")
