import httpx
from loguru import logger

async def fetch_website(url:str):
    headers = {
        "User-Agent": "SmartContentAggregator/1.0"
    }

    try:
        async with httpx.AsyncClient(
            headers=headers,
            timeout=httpx.Timeout(10.0, connect=5.0),
            follow_redirects=True
        ) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.text
    except httpx.RequestError as exc:
        logger.error(f"An error occurred while requesting {url}: {exc}")
        raise