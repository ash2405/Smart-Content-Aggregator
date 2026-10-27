
from pydantic import BaseModel, ConfigDict, HttpUrl


class SourceCreate(BaseModel):
    name: str
    url: HttpUrl


class SourceResponse(BaseModel):
    id: int
    name: str
    url: HttpUrl
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
