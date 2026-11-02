import httpx


class NewsAPIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_articles(self):

        try:
            async with httpx.AsyncClient() as client:

                response = await client.get(
                    self.base_url,
                    timeout=10.0
                )

                response.raise_for_status()

                return response.json()

        except httpx.TimeoutException:
            print("Error: External API request timed out.")
            raise

        except httpx.ConnectError:
            print("Error: Could not connect to external API.")
            raise

        except httpx.HTTPStatusError as exc:
            print(f"HTTP Error: {exc.response.status_code}")
            raise

        except httpx.RequestError as exc:
            print(f"Request Error: {exc}")
            raise
