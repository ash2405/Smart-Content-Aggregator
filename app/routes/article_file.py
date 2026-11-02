
from fastapi import APIRouter, Depends, File, UploadFile, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dependency import get_db
from app.schemas.article_file import ArticleFileResponse
from app.services.article_file import (
                                get_article_file_service, 
                                upload_article_file_service, 
                                download_article_file_service
                                )
router = APIRouter(
    prefix="/articles",
    tags=["Article Files"],
)


@router.post(
    "/{article_id}/files",
    response_model=ArticleFileResponse,
    status_code=201,
)
async def upload_article_file(
    article_id: int = Path(gt=0),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    return await upload_article_file_service(
        article_id=article_id,
        file=file,
        db=db,
    )

@router.get('/{article_id}')
async def get_article_file_by_id(
    article_id:int,
    db:AsyncSession = Depends(get_db)
):
    return get_article_file_service(db=db,article_id=article_id)

@router.get('/{article_id}/file/{file_id}',response_model=ArticleFileResponse)
async def article_file_download_by_id(
    file_id:int,
    article_id=int,
    db:AsyncSession = Depends(get_db),
):
    return await download_article_file_service(db=db,article_id=int(article_id), file_id=file_id)