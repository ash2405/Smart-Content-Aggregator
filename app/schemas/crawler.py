from pydantic import BaseModel

from app.schemas.article import ArticleResponse


class CrawlerRunResult(BaseModel):
    fetch_articles: int
    saved_articles_count: int
    skipped_duplicates_count: int
    save_articles: list[ArticleResponse]


class CrawlerResponse(BaseModel):
    success: bool
    message: str
    data: CrawlerRunResult


class CrawlerBGResponse(BaseModel):
    success:bool
    message:str
    data: None = None