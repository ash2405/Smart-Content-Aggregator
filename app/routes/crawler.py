from fastapi import Depends
from fastapi.routing import APIRouter
from app.core.dependency import get_db
from app.crawler.config import BOOKS_SOURCE
from app.crawler.runner import runner_cwarling

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.crawler import CrawlerResponse


router = APIRouter(
    prefix='/crawler',
    tags=["Crawler"]
        )

@router.post(
      '/run/{source_id}',
      response_model=CrawlerResponse)
async def trigger_crawler(
    source_id:int,
    db: AsyncSession = Depends(get_db)
):

   result =  await runner_cwarling(
        source_id=source_id,
        db=db,
        config=BOOKS_SOURCE
    )

   return {
        "success": True,
        "message": "Crawler executed successfully",
        "data": result,
    }