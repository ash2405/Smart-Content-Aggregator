from fastapi import APIRouter, File , UploadFile

from app.services.file_upload import file_upload_service

router = APIRouter(
    prefix='/files',
    tags=["Files"]
)

@router.post("/upload/{article_id}")
async def upload_file(
    article_id:int,
    file:UploadFile = File(...)
):
    return await file_upload_service(file=file)
    