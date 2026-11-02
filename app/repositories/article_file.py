
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.article_file import ArticleFile
from app.schemas.article_file import ArticleFileResponse

async def get_article_file_by_article_id(
        db:AsyncSession,
        article_id:int
)-> list[ArticleFileResponse]:
    result = await db.execute(
        select(ArticleFile).where(ArticleFile.article_id == article_id).order_by(ArticleFile.id.desc())
    )

    return list(result.scalar().all)

async def article_file_download(
        article_id:int,
        file_id:int,
        db:AsyncSession,
):
    result = await db.execute(
        select(ArticleFile).where(
            ArticleFile.article_id == article_id, ArticleFile.id == file_id
        )
    )

    return result.scalar_one_or_none()