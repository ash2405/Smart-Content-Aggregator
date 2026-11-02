
from datetime import datetime

from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        unique=True,
        nullable=False,
    )

    content: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    source_id: Mapped[int] = mapped_column(
        ForeignKey("sources.id"),
        nullable=False,
        index=True,
    )

    published_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    source: Mapped["Source"] = relationship(
        "Source",
        back_populates="articles",
    )

    category: Mapped[str | None] = mapped_column(
        String(240),
        nullable=True,
        index=True
    )

    status : Mapped[str] = mapped_column(
        String(240),
        default='Publish',
        nullable=False,
        index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    files: Mapped[list["ArticleFile"]] = relationship(
        "ArticleFile",
        back_populates='article',
        cascade='all, delete-orphan'

    )