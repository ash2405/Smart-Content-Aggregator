from fastapi import APIRouter, Depends, File , UploadFile

from app.core.auth import get_current_user
from app.services.file_upload import file_upload_service

router = APIRouter(
    prefix='/files',
    tags=["Files"]
)

@router.post("/upload/{article_id}")
async def upload_file(
    article_id:int,
    file:UploadFile = File(...),
    current_user = Depends(get_current_user)
):
    return await file_upload_service(file=file)
    