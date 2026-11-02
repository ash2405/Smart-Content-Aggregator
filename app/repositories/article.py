
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleListResponse, ArticleUpdate


async def create_article_item(
    article: Article,
    db: AsyncSession,
) -> Article:
    db.add(article)
    return article


async def get_article_by_id(
    article_id: int,
    db: AsyncSession,
) -> Article | None:
    result = await db.execute(
        select(Article).where(Article.id == article_id)
    )
    return result.scalar_one_or_none()


async def get_article_by_url(
    url: str,
    db: AsyncSession,
) -> Article | None:
    result = await db.execute(
        select(Article).where(Article.url == url)
    )
    return result.scalar_one_or_none()



async def get_all_articles(
    db: AsyncSession,
    skip: int = 1,
    limit: int = 10,
    search: str | None = None,
    source_id: int | None = None,
)-> ArticleListResponse:
    # Base queries
    query = select(Article)
    query_count = select(func.count()).select_from(Article)

    offset = (skip - 1) * limit

    if search:
        search_filter = Article.title.like(f"%{search}%")
        query = query.where(search_filter)
        query_count = query_count.where(search_filter)

    if source_id is not None:
        source_filter = Article.source_id == source_id
        query = query.where(source_filter)
        query_count = query_count.where(source_filter)

    query = query.order_by(Article.id).offset(offset).limit(limit)

    result = await db.execute(query)
    result_count = await db.execute(query_count)

    return {
        "items": list(result.scalars().all()),
        "total": result_count.scalar_one(),
        "limit":limit,
        "skip":skip
    }

async def update_article_item(article: Article, data: ArticleUpdate,db: AsyncSession) -> Article:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "url":
            setattr(article,field,str(value))
        else:
            setattr(article,field,value)
    await db.flush()
    return article
