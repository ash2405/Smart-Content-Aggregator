
from fastapi import APIRouter, Body, Depends, Query, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependency import get_db
from app.schemas.article import ArticleCreate, ArticleListResponse, ArticleResponse, ArticleUpdate
from app.services.article import (
    create_article_service,
    delete_article_service,
    get_articles_service,
    get_article_by_id_service,
    save_external_article,
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


@router.get("/", response_model=ArticleListResponse)
async def get_articles(
    limit: int = Query(default=10, ge=1, le=100),
    skip: int = Query(default=1, ge=1),
    search: str | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
    source_id: int | None = Query(default=None, gt=0),
):
    return await get_articles_service(db, limit, skip, search, source_id)


@router.get("/{article_id}", response_model=ArticleResponse)
async def get_article_by_id(
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await get_article_by_id_service(article_id, db)


@router.put("/{article_id}", response_model=ArticleResponse)
async def update_article(
    article_data: ArticleUpdate = Body(...),
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

@router.post('/external')
async def create_external_artcile(
    source_id:int,
    db:AsyncSession=Depends(get_db)
):
    return await save_external_article(
        source_id=source_id,
        db=db
    )