from typing import Literal

from pydantic import BaseModel, Field


class NewsIngestRequest(BaseModel):
    source: str = Field(..., description="News source identifier")
    lang: Literal["ar", "en"] = Field(..., description="Language code")
    title: str
    body: str
    symbols: list[str] = Field(default_factory=list)


class NewsIngestResponse(BaseModel):
    accepted: bool
    dedup_group_id: str
    sentiment: Literal["positive", "negative", "neutral"]
    impact_score: int = Field(..., ge=1, le=10)
    normalized_title_ar: str | None = None
    normalized_title_en: str | None = None


class AskNewsRequest(BaseModel):
    news_id: str
    question: str
    lang: Literal["ar", "en"] = "ar"


class AskNewsResponse(BaseModel):
    answer: str
    confidence: float = Field(..., ge=0, le=1)
