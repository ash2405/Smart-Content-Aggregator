from app.integrations.news_client import NewsAPIClient
from app.core.config import settings
from app.schemas.external_news import ExternalArticleSchema

async def fetch_external_articles(source_id:int =1):
    client =  NewsAPIClient(settings.news_api_url)
    articles = await client.get_articles()
    validate_arr = [
        transform_external_article(article=ExternalArticleSchema.model_validate(article),source_id=source_id) for article in articles
    ]


    print("first valid article",validate_arr[0])
    return validate_arr

def transform_external_article(
        article:ExternalArticleSchema,
        source_id:int
)-> dict:
    return{
        "title": article.title,
        "url":f"{settings.news_api_url}/{article.external_id}",
        "content":article.content,
        "source_id":source_id,
        "published_at":None
    }