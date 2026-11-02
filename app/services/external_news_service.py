from app.integrations.news_client import NewsAPIClient
from app.core.config import settings

async def fetch_external_articles():
    client =  NewsAPIClient(settings.news_api_url)
    articles = await client.get_articles()
    return articles