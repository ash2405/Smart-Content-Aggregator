from app.core.redis import redis_client

async def set_cache(key:str,value:str,ttl:int):
    return await redis_client.set(key,value,ex=ttl)
    


# Understand the code
# await redis_client.set("article:1", "FastAPI Tutorial")
   

# key: Unique identifier.
# value: Data jo store karna hai.
# await: Redis ke asynchronous operation ka wait karta hai.
# response: Successful SET par Redis normally True return karta hai.

# -----------------------------------------------

async def get_cache(key:str):
    return await redis_client.get(key)


async def delete_cache(key:str):
    return await redis_client.delete(key)

async def invalidate_cache(key:str):
    return await delete_cache(key)

async def invalidate_article_list_cache():
    async for key in redis_client.scan_iter(
        match="articles:list:*"
    ):
        await redis_client.delete(key)