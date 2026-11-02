from pydantic import BaseModel, Field, ConfigDict


class ExternalArticleSchema(BaseModel):
    external_id : int = Field(alias="id")
    title:str
    content: str = Field(alias="body")
    model_config = ConfigDict(
        extra="ignore",
        populate_by_name=True
    )

# external_id — external API ka id field receive karega.

# Field(alias="id") — API mein key id hai, hamare schema mein naam external_id hai.

# content — API ka body field receive karega.

# extra="ignore" — API ka userId field abhi ignore hoga.

# populate_by_name=True — alias aur Python field name dono se data populate ho sakta hai.
