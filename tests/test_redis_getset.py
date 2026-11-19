import asyncio

from app.services.redis import delete_cache, get_cache, set_cache

from app.core.redis import redis_client


# async def main():
#     # Set
#     response = await set_cache(
#         key='article1',
#         value="article detail",
#         ttl=60
#     )
#     print("Set Cache Response : ", response)


#     # Get
#     getRes = await get_cache(key="article")
#     print("Get Cache Response : ", getRes)

#     # Delete
#     delRes = await delete_cache(key="article1")
#     print("Delete  Cache Response : ", delRes)
    
#     # Get After Delete
#     getRes1 = await get_cache(key="article1")
#     print("Get After Delete Cache Response : ", getRes1)

#     redis_client.aclose()


async def main():
    # Set
    await set_cache(
        key="article1",
        value="article detail",
        ttl=1
    )

    print("get detail before expire : ", await get_cache(key="article1"))

    await asyncio.sleep(3)
    
    print("get detail after expire : ", await get_cache(key="article1"))

    await redis_client.aclose()

asyncio.run(main())
