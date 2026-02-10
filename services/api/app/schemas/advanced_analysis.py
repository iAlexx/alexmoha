from pydantic import BaseModel, Field


class HeatmapItem(BaseModel):
    symbol: str
    change_pct: float
    momentum_score: float


class HeatmapResponse(BaseModel):
    strongest: list[HeatmapItem]
    weakest: list[HeatmapItem]
    interval_hours: int = 4


class DivergenceAlertRequest(BaseModel):
    symbol: str
    news_impact_score: int = Field(..., ge=1, le=10)
    price_move_pct: float


class DivergenceAlertResponse(BaseModel):
    divergence: bool
    message: str


class InstantBacktestRequest(BaseModel):
    symbol: str
    event_type: str


class InstantBacktestResponse(BaseModel):
    chart_hint_url: str
    median_move_pips: float


class LiquidityLevelRequest(BaseModel):
    symbol: str
    current_price: float
    major_level: float


class LiquidityLevelResponse(BaseModel):
    near_level: bool
    distance_pct: float
    message: str
