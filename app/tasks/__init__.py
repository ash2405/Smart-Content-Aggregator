import asyncio
from sqlalchemy import select

from app.core.celery_app import celery_app
from app.db.session import AsyncSessionLocal
from app.enums.job_status import JobStatus
from app.models.job import Job


@celery_app.task
def test_celery_task():
    return "Celery is working successfully!"

# Background Jobs with Celery
# bind = True → Celery task instance ko self ke through provide karta hai.
@celery_app.task(
        bind=True,
        max_retries=3,
        default_retry_delay=10
        )
def process_article_id(self,article_id:int):

    try:
        print(f"Artilce id for the porcess id {article_id}")

        if article_id == 888:
            raise ConnectionError("Temporary network error!")

        if article_id == 999:
            raise ValueError("Article processing failed!")

        return{
            "message":"return from Process article",
            "article_id":article_id
        }
    
    except ValueError:
        raise
    
    except Exception as exc:
        # self.retry() → task ko retry karne ke liye schedule karta hai.
        raise self.retry(exc=exc , countdown=5)


# For job id
@celery_app.task
def crawl_articles_task(job_id: int):
    # PENDING se RUNNING status update
    # Can't use Depends(get_db) that's why directly use AsyncSessionLocal here

    # asyncio.run()         :	Synchronous Celery task ke andar async code execute karta hai.
    # run_task()            :	Async function create kiya.
    # AsyncSessionLocal()	:   Database session create karta hai.
    # async with	        :   Session ko manage karta hai aur block exit hone par close karta hai.
    async def run_db():
        async with AsyncSessionLocal() as db:
            print(f"Database session created for Job ID: {job_id}")
            result = await db.execute(
                select(Job).where(Job.id == job_id)
            )

            job = result.scalar_one_or_none()

            if job is not None:
                print(f"Job detail",job)

                job.status = JobStatus.RUNNING

                await db.commit()
                await db.refresh(job)

                print(f"Job Status",job.status)
                print(f"Crawling started for job.status----------D: {job.status}")
                try:
                    # Add below code
                    job.status = JobStatus.COMPLETED

                    await db.commit()
                    await db.refresh(job)

                    print("Job completed:", job.status)

                except Exception as exc:
                    job.status = JobStatus.FAILED
                    await db.commit()
                    raise exc

    asyncio.run(run_db())
            

    return {
        "message": "Crawling task executed",
        "job_id": job_id
    }