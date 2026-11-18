import uuid
from pathlib import Path

from fastapi import UploadFile

from app.core.config import settings
from app.exceptions.exceptions_log import BadRequestException

ALLOWED_TYPES = {
    "application/pdf": ".pdf",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp"
}

async def file_upload_service(file:UploadFile):

    # get the file content type to check the valid file only
    content_type = file.content_type

    if content_type not in ALLOWED_TYPES:
        raise BadRequestException(f"{content_type} is not valid type to upload file.")

    store_name = f"{uuid.uuid4().hex}{ALLOWED_TYPES[content_type]}"

    # create path to upload the file
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir/store_name

    max_size = settings.max_upload_size
    file_size = 0

    try:
            # open(file_path, "wb")
            # w = Write mode
            # b = Binary mode
        with open(file_path,'wb') as destination:
            while chunk := await file.read(1024 * 1024):
                file_size += len(chunk)

                if file_size > max_size:
                    raise BadRequestException(
                         "File size exceeds 5 MB limit"
                    )

            destination.write(chunk)

            if file_size == 0:
                    raise BadRequestException(f"Empty file not allowed")


            return{
                    'success': True,
                    'message':"File uploaded",
                    "article_id": 1,
                    "file_name":file.filename,
                    "content_type":file.content_type
                }

    except Exception:
            if file_path.exists():
               file_path.unlink()
            raise