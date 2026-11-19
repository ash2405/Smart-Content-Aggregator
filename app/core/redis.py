from asyncio.log import logger

from redis.asyncio import Redis
from app.core.config import settings

redis_client = Redis.from_url(
    settings.redis_url,
    decode_responses = True
)

# Redis.from_url() — Redis URL se connection client create karta hai.
# settings.redis_url — .env se Redis URL leta hai.
# decode_responses=True — Redis se returned strings ko bytes ke bajaye normal Python strings mein deta hai.

# Test Redis Connection

async def check_redis_connection():
    try:
        response = await redis_client.ping()

        if response:
            print(f"Redis Connection Successfully Done!")
            # Redis connection error handling
            logger.info("Redis connected successfully!")

        return True
    
    except Exception as exc:
        print(f"{exc} error during Redis Connection")
        # Redis connection error handling
        logger.exception("Redis connection failed!")
        raise
        