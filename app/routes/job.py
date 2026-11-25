from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependency import get_db
from app.schemas.job import JobResponse
from app.services.job import create_job_service, get_job_by_id, update_job_service
from app.tasks import crawl_articles_task



router = APIRouter(
    prefix='/job',
    tags=["Job"]
)

@router.post('/crawl')
async def creat_task_job(
    db:AsyncSession = Depends(get_db)
):
    job =  await create_job_service(db=db)

    task = crawl_articles_task.apply_async(
        kwargs={"job_id": job.id}
    )

    print("Job ID:", job.id)
    print("Celery Task ID:", task.id)
    print("Task State:", task.state)
    
    update_job = await update_job_service(
        db=db,
        task_id=task.id,
        job=job
    )

    return update_job


@router.get('/crawl/{job_id}')
async def get_job_info(
    job_id:int,
    db: AsyncSession = Depends(get_db),
    ):
    return await get_job_by_id(
        db=db,
        job_id=job_id
    )