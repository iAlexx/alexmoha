from typing import Literal

from pydantic import BaseModel, Field


class TrustScoreRequest(BaseModel):
    source_reliability: float = Field(..., ge=0, le=1)
    source_confirmations: int = Field(..., ge=0)
    freshness_minutes: int = Field(..., ge=0)
    price_alignment: float = Field(..., ge=0, le=1)


class TrustScoreResponse(BaseModel):
    trust_score: int = Field(..., ge=0, le=100)
    confidence_band: Literal['low', 'medium', 'high']


class TradeReadinessRequest(BaseModel):
    impact_score: int = Field(..., ge=1, le=10)
    liquidity_score: float = Field(..., ge=0, le=1)
    volatility_score: float = Field(..., ge=0, le=1)
    level_proximity_score: float = Field(..., ge=0, le=1)


class TradeReadinessResponse(BaseModel):
    readiness_score: float = Field(..., ge=0, le=10)
    action_bias: Literal['wait', 'monitor', 'ready']


class PersonalizationRequest(BaseModel):
    user_id: str
    symbols: list[str] = Field(default_factory=list)
    quiet_hours_utc: list[int] = Field(default_factory=list)
    analysis_mode: Literal['technical', 'fundamental', 'hybrid'] = 'hybrid'
    alert_intensity: Literal['low', 'normal', 'high'] = 'normal'


class PersonalizationResponse(BaseModel):
    user_id: str
    applied: bool


class PersonalizationProfileResponse(BaseModel):
    user_id: str
    symbols: list[str]
    quiet_hours_utc: list[int]
    analysis_mode: str
    alert_intensity: str


class PostEventAccuracyRequest(BaseModel):
    event_id: str
    predicted_direction: Literal['up', 'down', 'neutral']
    actual_direction: Literal['up', 'down', 'neutral']
    predicted_move_pips: float = 0
    actual_move_pips: float = 0


class PostEventAccuracyResponse(BaseModel):
    event_id: str
    direction_correct: bool
    magnitude_error_pct: float
    accuracy_score: float = Field(..., ge=0, le=100)


class ChannelGrowthRequest(BaseModel):
    channel_id: str
    posts_last_7d: int = Field(..., ge=0)
    reactions_last_7d: int = Field(..., ge=0)
    shares_last_7d: int = Field(..., ge=0)


class ChannelGrowthResponse(BaseModel):
    channel_id: str
    engagement_score: float
    best_posting_window_utc: str
    content_recommendations: list[str]
