from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class SessionMasterRequest(BaseModel):
    session: Literal['london', 'new_york', 'tokyo']
    run_at: datetime | None = None


class SessionLiquidityPair(BaseModel):
    symbol: str
    expected_volatility: float = Field(..., ge=0)
    reason: str


class SessionMasterResponse(BaseModel):
    session: str
    liquidity_forecast: Literal['low', 'moderate', 'high']
    top_pairs: list[SessionLiquidityPair]


class GapDetectorRequest(BaseModel):
    symbol: str
    friday_close: float
    monday_open: float


class GapDetectorResponse(BaseModel):
    symbol: str
    gap_points: float
    gap_percent: float
    close_probability: float = Field(..., ge=0, le=1)


class NoiseFilterRequest(BaseModel):
    high_impact_mode: bool
    incoming_impact_score: int = Field(..., ge=1, le=10)


class NoiseFilterResponse(BaseModel):
    allow_alert: bool
    policy: str


class BacktestNewsRequest(BaseModel):
    asset: str
    event_type: str
    lookback_days: int = Field(default=365, ge=30, le=1460)


class BacktestNewsResponse(BaseModel):
    asset: str
    event_type: str
    avg_up_move_pips: float
    avg_down_move_pips: float
    samples: int


class FakeNewsCheckRequest(BaseModel):
    headline: str
    trusted_sources_matched: int = Field(..., ge=0)


class FakeNewsCheckResponse(BaseModel):
    verified_breaking: bool
    confidence: float = Field(..., ge=0, le=1)
    note: str
