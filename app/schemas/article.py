
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class ArticleCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=300,
        examples=['testing']
    )
    url: HttpUrl = Field(
        examples=["https://example.com/fastapi-guide"],
    )
    content: str | None = Field(
        default=None,
        examples=["A practical guide to building APIs with FastAPI."],
    )
    source_id: int = Field(
         gt=0,
        examples=[1],
    )
    published_at: datetime | None = Field(
         default=None,
        examples=["2026-10-20T10:30:00Z"],
    )
    category: str | None = Field(
        default=None,
        max_length=100,
        examples=["Technology"],
    )
    status: Literal["Draft", "Published", "Archived"] = Field(
        default="published",
        examples=["published"],
    )



class ArticleResponse(ArticleCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
    


class ArticleListResponse(BaseModel):
    items: list[ArticleResponse]
    total: int
    skip: int
    limit: int


class ArticleUpdate(BaseModel):
    title:str = Field(default=None , min_length=1, max_length=300)
    url: HttpUrl | None = None
    content: str | None = None
    source_id:int = Field(default=None,ge=0)
    published_at: datetime | None = None
    category: str | None
    status: str
    created_at: datetime

    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "title":"Update schema"
            }
        }
    )
