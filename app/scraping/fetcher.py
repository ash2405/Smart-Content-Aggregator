import asyncio
import httpx
from loguru import logger


async def fetcher_html(url: str) -> str:
    headers = {
        "User-Agent": "SmartContentAggregator/1.0"
    }

    max_retries = 3

    for attempt in range(1, max_retries + 1):

        try:
            async with httpx.AsyncClient(
                headers=headers,
                timeout=10.0,
                follow_redirects=True
            ) as client:

                response = await client.get(url)
                response.raise_for_status()

                logger.info(f"Successfully fetched: {url}")

                return response.text

        except httpx.HTTPStatusError as exc:

            status_code = exc.response.status_code

            # Retry only for temporary server/rate-limit errors
            if status_code != 429 and status_code < 500:
                logger.error(
                    f"Non-retryable HTTP error: {status_code}"
                )
                raise

            logger.warning(
                f"HTTP {status_code}, attempt {attempt}"
            )

        except (
            httpx.TimeoutException,
            httpx.ConnectError,
            httpx.RemoteProtocolError
        ) as exc:

            logger.warning(
                f"Request failed, attempt {attempt}: {exc}"
            )

        if attempt < max_retries:
            wait_time = 2 ** (attempt - 1)

            logger.info(
                f"Retrying after {wait_time} seconds..."
            )

            await asyncio.sleep(wait_time)

    raise httpx.RequestError(
        f"Failed to fetch {url} after {max_retries} attempts"
    )