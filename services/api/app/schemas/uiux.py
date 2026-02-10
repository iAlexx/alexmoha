from pydantic import BaseModel


class InlineNewsControlsRequest(BaseModel):
    news_id: str


class InlineNewsControlsResponse(BaseModel):
    buttons: list[dict[str, str]]
