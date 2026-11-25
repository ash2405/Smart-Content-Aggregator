from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.db.base import Base
from app.enums.job_status import JobStatus


class Job(Base):

    __tablename__ = "jobs"

    id : Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    task_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True
    )

    status: Mapped[str] = mapped_column(
        String(255),
        default=JobStatus.PENDING,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
