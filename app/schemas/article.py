
from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl


class ArticleCreate(BaseModel):
    title: str
    url: HttpUrl
    content: str | None = None
    source_id: int
    published_at: datetime | None = None


class ArticleResponse(ArticleCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
