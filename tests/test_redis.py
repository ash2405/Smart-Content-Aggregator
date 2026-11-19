
import asyncio

from app.core.redis import redis_client,check_redis_connection

async def main():
    await check_redis_connection()
    await redis_client.aclose()


asyncio.run(main())
