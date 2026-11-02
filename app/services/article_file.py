import uuid

from fastapi import  UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from pathlib import Path
from app.exceptions.exceptions_log import BadRequestException, NotFoundException
from app.models.article_file import ArticleFile
from app.repositories.article import get_article_by_id
from app.core.config import settings
from app.repositories.article_file import get_article_file_by_article_id
from app.repositories.article_file import article_file_download
ALLOWED_TYPES = {
    "application/pdf": ".pdf",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
}

async def upload_article_file_service(
        article_id:int,
        db:AsyncSession,
        file: UploadFile

)-> ArticleFile:

   # get article detail
   article =  await get_article_by_id(article_id,db)
   
   # check article is present
   if article is None:
        raise NotFoundException(f"Article with id {article_id} not found")
   
   # get file content type
   content_type = file.content_type
   
   # check the content type is valid 
   if content_type not in ALLOWED_TYPES:
       raise BadRequestException(f"{content_type} is not valid")
   
   # get path to upload file
   upload_dir = Path(settings.upload_dir)
   upload_dir.mkdir(parents=True, exist_ok=True)

   # get unique name of file
   stored_name = f"{uuid.uuid4().hex}{ALLOWED_TYPES[content_type]}"

   file_path= upload_dir/stored_name

   max_size = settings.max_upload_size
   file_size = 0

   try:
       with file_path.open('wb') as output:
           # read and store the file in 1MB chunk or read full file at a time
           while chunk := await file.read(1024 * 1024):
               file_size += len(chunk)

               if file_size > max_size:
                   raise BadRequestException("Invaid image size")
               output.write(chunk)

       if file_size == 0:
           raise BadRequestException("Empty files are not allowed")

       article_file = ArticleFile(
           article_id=article_id,
           file_name=Path(file.filename or "Upload").name,
           file_path=str(file_path),
           content_type=content_type,
           file_size=file_size,
       )

       db.add(article_file)
       await db.commit()
       await db.refresh(article_file)
       return article_file
   except:
       await db.rollback()
       raise


async def get_article_file_service(
        db:AsyncSession,
        article_id:int
):
    article = await get_article_by_id(db=db,article_id=article_id)

    if article is None:
        raise NotFoundException(f"Article of id {article_id} is not found")

    return await get_article_file_by_article_id(db=db,article_id=article_id)


async def download_article_file_service(
        article_id:int,
        file_id:int,
        db:AsyncSession
):

    # article = await get_article_by_id(db=db,article_id=article_id)

    # if article is None:
    #     raise NotFoundException(f"Article of id {article_id} is not found")

    try:
        return await article_file_download(
            db=db,
            article_id=article_id,
            file_id=file_id
        )
    except:
        await db.rollback()
        raise
