
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.article import Article
from app.schemas.article import ArticleCreate


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
    skip: int = 0,
    limit: int = 10,
) -> list[Article]:
    result = await db.execute(
        select(Article)
        .order_by(Article.id)
        .offset(skip)
        .limit(limit)
    )
    return list(result.scalars().all())

async def update_article_item(article: Article, data: ArticleCreate,db: AsyncSession) -> Article:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "url":
            setattr(article,field,str(value))
        else:
            setattr(article,field,value)
    await db.flush()
    return article
