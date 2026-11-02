import asyncio

from app.core.config import settings
from app.services.external_news_service import fetch_external_articles
async def main():
    articles = await fetch_external_articles()

    print("Total articles:", len(articles))
    print("First article:")
    print(articles[0])


if __name__ == "__main__":
    asyncio.run(main())