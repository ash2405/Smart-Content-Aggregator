
from fastapi import APIRouter, Depends, Query, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependency import get_db
from app.schemas.article import ArticleCreate, ArticleResponse
from app.services.article import (
    create_article_service,
    delete_article_service,
    get_articles_service,
    get_article_by_id_service,
    update_article_service,
)

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
)


@router.post(
    "/",
    response_model=ArticleResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_article(
    article: ArticleCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_article_service(article, db)


@router.get("/", response_model=list[ArticleResponse])
async def get_articles(
    limit: int = Query(default=10, ge=1, le=100),
    skip: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    return await get_articles_service(db, limit, skip)


@router.get("/{article_id}", response_model=ArticleResponse)
async def get_article_by_id(
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await get_article_by_id_service(article_id, db)


@router.put("/{article_id}", response_model=ArticleResponse)
async def update_article(
    article_data: ArticleCreate,
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await update_article_service(article_id, article_data, db)

@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await delete_article_service(article_id, db)