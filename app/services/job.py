from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.enums.job_status import JobStatus
from app.exceptions.exceptions_log import NotFoundException
from app.models.job import Job

async def create_job_service(
        db:AsyncSession
)-> Job:
    job = Job(
        status = JobStatus.PENDING 
    )

    db.add(job)
    await db.commit()
    await db.refresh(job)

    return job

async def update_job_service(
        db:AsyncSession,
        task_id:int,
        job : Job
):
    job.task_id = task_id
    await db.commit()
    await db.refresh(job)

    return job


async def get_job_by_id(db:AsyncSession,job_id):
    result = await db.execute(
        select(Job).where(Job.id == job_id)
    )

    if result is None:
        raise NotFoundException("Job not found")

    return result.scalar_one_or_none()
