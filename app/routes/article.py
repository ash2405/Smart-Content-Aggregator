
from fastapi import APIRouter, Body, Depends, Query, Path, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from celery.result import AsyncResult
from app.core.celery_app import celery_app
from app.core.rate_limiter import limiter
from app.core.dependency import get_db
from app.schemas.article import ArticleCreate, ArticleListResponse, ArticleResponse, ArticleUpdate
from app.services.article import (
    create_article_service,
    delete_article_service,
    get_articles_service,
    get_article_by_id_service,
    save_external_article,
    update_article_service,
)
from app.services.redis import get_cache, set_cache
from app.tasks import process_article_id

router = APIRouter(
    prefix="/articles",
    tags=["articles"],
)


@router.post(
    "/",
    response_model=ArticleResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_article(
    article: ArticleCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_article_service(article, db)


@router.get("/", response_model=ArticleListResponse)
@limiter.limit("2/minute")
async def get_articles(
    request:Request,
    limit: int = Query(default=10, ge=1, le=100),
    skip: int = Query(default=1, ge=1),
    search: str | None = Query(default=None),
    db: AsyncSession = Depends(get_db),
    source_id: int | None = Query(default=None, gt=0),
):
    return await get_articles_service(db, limit, skip, search, source_id)





@router.put("/{article_id}", response_model=ArticleUpdate)
async def update_article(
    article_data: ArticleUpdate = Body(...),
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await update_article_service(article_id, article_data, db)

@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await delete_article_service(article_id, db)

@router.post('/external')
async def create_external_artcile(
    source_id:int,
    db:AsyncSession=Depends(get_db)
):
    return await save_external_article(
        source_id=source_id,
        db=db
    )

@router.get("/t/{article_id}", response_model=ArticleResponse)
@limiter.limit("2/minute")
async def get_article_by_id(
    request:Request,
    article_id: int = Path(gt=0),
    db: AsyncSession = Depends(get_db),
):
    return await get_article_by_id_service(article_id, db)

# Celery process task for process article
@router.post("/process")
async def process_article(
    article_id:int
):
    try:
        task = process_article_id.delay(article_id=article_id)
        print('task response - ', task)

        await set_cache(
            key=f"article:task:{article_id}",
            value=task.id,
            ttl=86400
         )

        return {
            "message": "Article processing started",
            "task_id": task.id,
            "article_id": article_id
        }
    except Exception as exc:
        raise exc

# Check task status 
@router.get("/status/{article_id}")
async def check_task_status(
    article_id
):
    task_id = await get_cache(
        key=f"article:task:{article_id}"
    )

    if not task_id:
        return {
            "message": "No task found for this article"
        }
    
    task_result = AsyncResult(
        task_id,
        app = celery_app
    )
 

    # AsyncResult() — task ka result retrieve karta hai.
    # task_id — specific task identify karta hai.
    # status — task ka current status deta hai.
    # result — task ka returned data deta hai.
    if task_result.failed():
        return {
            "article_id": article_id,
            "task_id": task_id,
            "status": task_result.status,
            "error": str(task_result.result)
        }

    return{
        "article_id":task_result.id,
        "status":task_result.status,
        "result":task_result.result
    }