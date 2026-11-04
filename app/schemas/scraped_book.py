from pydantic import BaseModel, Field, HttpUrl

class ScrapedBookSchema(BaseModel):
    title: str = Field(min_length=1)
    price: str
    availability: str
    url: HttpUrl