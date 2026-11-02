
from pydantic import BaseModel, ConfigDict


class ArticleFileResponse(BaseModel):
    id: int
    article_id: int
    file_name: str
    content_type: str | None
    file_size: int

    model_config = ConfigDict(from_attributes=True)
