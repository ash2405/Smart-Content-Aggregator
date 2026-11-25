from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums.job_status import JobStatus


class JobResponse(BaseModel):

    id: int
    task_id: str | None
    status: JobStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)