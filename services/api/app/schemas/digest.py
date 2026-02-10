from pydantic import BaseModel


class DailyDigestRequest(BaseModel):
    date: str
    headlines: list[str]


class DailyDigestResponse(BaseModel):
    digest_markdown: str
    watchlist_tomorrow: list[str]
