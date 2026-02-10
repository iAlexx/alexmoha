from typing import Literal

from pydantic import BaseModel, Field


class CorrelationRadarRequest(BaseModel):
    trigger_symbol: str
    trigger_move_pct: float = Field(..., description="Observed move on trigger symbol")


class CorrelationOpportunity(BaseModel):
    symbol: str
    expected_direction: Literal["up", "down"]
    confidence: float = Field(..., ge=0, le=1)


class CorrelationRadarResponse(BaseModel):
    trigger_symbol: str
    opportunities: list[CorrelationOpportunity]


class WhaleDetectionRequest(BaseModel):
    asset: str
    transfer_usd: float
    price_spike_pct: float


class WhaleDetectionResponse(BaseModel):
    suspicious: bool
    risk_level: Literal["low", "medium", "high", "critical"]
    reason: str
