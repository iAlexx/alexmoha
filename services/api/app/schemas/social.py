from typing import Literal

from pydantic import BaseModel, Field


class SentimentVoteRequest(BaseModel):
    news_id: str
    user_id: str
    vote: Literal['bullish', 'bearish']


class SentimentVoteResponse(BaseModel):
    news_id: str
    bullish: int
    bearish: int
    community_bias: Literal['bullish', 'bearish', 'neutral']


class WhaleWatchRequest(BaseModel):
    asset: str
    transfer_usd: float = Field(..., ge=0)
    related_news_id: str | None = None


class WhaleWatchResponse(BaseModel):
    triggered: bool
    level: Literal['info', 'watch', 'alert', 'critical']
    relation_note: str
