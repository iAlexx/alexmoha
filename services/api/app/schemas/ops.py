from pydantic import BaseModel, Field


class NoisePreferenceRequest(BaseModel):
    user_id: str
    min_move_pct_5m: float = Field(default=0.5, ge=0)
    critical_mode: bool = False


class NoisePreferenceResponse(BaseModel):
    user_id: str
    min_move_pct_5m: float
    critical_mode: bool


class AlertEligibilityRequest(BaseModel):
    user_id: str
    move_pct_5m: float
    trend_changer: bool = False


class AlertEligibilityResponse(BaseModel):
    send_alert: bool
    reason: str


class PostMarketInsightRequest(BaseModel):
    date: str
    vip_only: bool = True
    headlines: list[str]


class PostMarketInsightResponse(BaseModel):
    report_title: str
    insights: list[str]


class TelegramWebAppConfigResponse(BaseModel):
    enabled: bool
    webapp_url: str
    features: list[str]
