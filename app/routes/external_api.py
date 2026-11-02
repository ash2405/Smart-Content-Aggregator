from fastapi import APIRouter

from app.services.external_news_service import fetch_external_articles

router = APIRouter(
    prefix="/external-news",
    tags=["External News"],
)


@router.get("/")
async def get_external_articles():
    articles = await fetch_external_articles()

    return {
        "success": True,
        "total": len(articles),
        "articles": articles,
    }