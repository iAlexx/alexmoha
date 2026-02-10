from fastapi import APIRouter

from app.schemas.ops import (
    AlertEligibilityRequest,
    AlertEligibilityResponse,
    NoisePreferenceRequest,
    NoisePreferenceResponse,
    PostMarketInsightRequest,
    PostMarketInsightResponse,
    TelegramWebAppConfigResponse,
)
from app.services.ops import ops_service

router = APIRouter()


@router.put('/noise-preferences', response_model=NoisePreferenceResponse)
def set_noise_preferences(payload: NoisePreferenceRequest) -> NoisePreferenceResponse:
    profile = ops_service.set_noise_profile(payload.user_id, payload.min_move_pct_5m, payload.critical_mode)
    return NoisePreferenceResponse(user_id=payload.user_id, **profile)


@router.post('/alert-eligibility', response_model=AlertEligibilityResponse)
def alert_eligibility(payload: AlertEligibilityRequest) -> AlertEligibilityResponse:
    send, reason = ops_service.alert_eligibility(payload.user_id, payload.move_pct_5m, payload.trend_changer)
    return AlertEligibilityResponse(send_alert=send, reason=reason)


@router.post('/post-market-insights', response_model=PostMarketInsightResponse)
def post_market_insights(payload: PostMarketInsightRequest) -> PostMarketInsightResponse:
    title, insights = ops_service.post_market_insight(payload.date, payload.headlines)
    return PostMarketInsightResponse(report_title=title, insights=insights)


@router.get('/telegram-webapp', response_model=TelegramWebAppConfigResponse)
def telegram_webapp() -> TelegramWebAppConfigResponse:
    cfg = ops_service.telegram_webapp_config()
    return TelegramWebAppConfigResponse(**cfg)
