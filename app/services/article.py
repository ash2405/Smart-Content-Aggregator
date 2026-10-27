
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.article import Article
from app.schemas.article import ArticleCreate
from app.repositories.article import (
    create_article_item,
    get_article_by_id,
    get_article_by_url,
    get_all_articles,
    update_article_item,
)
from app.repositories.source import get_source_by_id
from app.exceptions.exceptions_log import (
    NotFoundException,
    ConflictException,
)


async def create_article_service(
    article: ArticleCreate,
    db: AsyncSession,
) -> Article:
    # Check whether the source exists
    source = await get_source_by_id(article.source_id, db)

    if source is None:
        raise NotFoundException(
            f"Source with id {article.source_id} not found."
        )

    # Check for duplicate article URL
    article_url = str(article.url)
    existing_article = await get_article_by_url(article_url, db)

    if existing_article is not None:
        raise ConflictException(
            "An article with this URL already exists."
        )

    try:
        new_article = Article(
            title=article.title,
            url=article_url,
            content=article.content,
            source_id=article.source_id,
            published_at=article.published_at,
        )

        created_article = await create_article_item(new_article, db)
        await db.commit()
        await db.refresh(created_article)

        return created_article

    except Exception:
        await db.rollback()
        raise


async def get_articles_service(
    db: AsyncSession,
    limit: int = 10,
    skip: int = 0,
) -> list[Article]:
    return await get_all_articles(db, skip=skip, limit=limit)


async def get_article_by_id_service(
    article_id: int,
    db: AsyncSession,
) -> Article:
    article = await get_article_by_id(article_id, db)

    if article is None:
        raise NotFoundException(
            f"Article with id {article_id} not found."
        )

    return article

async def update_article_service(
    article_id: int,
    article_data: ArticleCreate,
    db: AsyncSession,
) -> Article:
    # Fetch the existing article
    existing_article = await get_article_by_id(article_id, db)

    if existing_article is None:
        raise NotFoundException(
            f"Article with id {article_id} not found."
        )

    # Check for duplicate article URL if the URL is being updated
    duplicate_article = await get_article_by_url(str(article_data.url), db)
    if duplicate_article is not None:
        raise ConflictException(
            "An article with this URL already exists."
        )

    try:
        updated_article = await update_article_item(existing_article, article_data, db)
        await db.commit()
        await db.refresh(updated_article)

        return updated_article

    except Exception:
        await db.rollback()
        raise

async def delete_article_service(
    article_id: int,
    db: AsyncSession,
) -> None:
    # Fetch the existing article
    existing_article = await get_article_by_id(article_id, db)

    if existing_article is None:
        raise NotFoundException(
            f"Article with id {article_id} not found."
        )

    try:
        await db.delete(existing_article)
        await db.commit()

    except Exception:
        await db.rollback()
        raise