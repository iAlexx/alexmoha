from fastapi import APIRouter

from app.schemas.excellence import (
    ChannelGrowthRequest,
    ChannelGrowthResponse,
    PersonalizationProfileResponse,
    PersonalizationRequest,
    PersonalizationResponse,
    PostEventAccuracyRequest,
    PostEventAccuracyResponse,
    TradeReadinessRequest,
    TradeReadinessResponse,
    TrustScoreRequest,
    TrustScoreResponse,
)
from app.services.excellence import excellence_service

router = APIRouter()


@router.post('/trust-score', response_model=TrustScoreResponse)
def trust_score(payload: TrustScoreRequest) -> TrustScoreResponse:
    return excellence_service.trust_score(
        payload.source_reliability,
        payload.source_confirmations,
        payload.freshness_minutes,
        payload.price_alignment,
    )


@router.post('/trade-readiness', response_model=TradeReadinessResponse)
def trade_readiness(payload: TradeReadinessRequest) -> TradeReadinessResponse:
    return excellence_service.trade_readiness(
        payload.impact_score,
        payload.liquidity_score,
        payload.volatility_score,
        payload.level_proximity_score,
    )


@router.put('/personalization', response_model=PersonalizationResponse)
def set_personalization(payload: PersonalizationRequest) -> PersonalizationResponse:
    excellence_service.save_profile(
        payload.user_id,
        payload.symbols,
        payload.quiet_hours_utc,
        payload.analysis_mode,
        payload.alert_intensity,
    )
    return PersonalizationResponse(user_id=payload.user_id, applied=True)


@router.get('/personalization/{user_id}', response_model=PersonalizationProfileResponse)
def get_personalization(user_id: str) -> PersonalizationProfileResponse:
    return excellence_service.get_profile(user_id)


@router.post('/post-event-accuracy', response_model=PostEventAccuracyResponse)
def post_event_accuracy(payload: PostEventAccuracyRequest) -> PostEventAccuracyResponse:
    return excellence_service.post_event_accuracy(
        payload.event_id,
        payload.predicted_direction,
        payload.actual_direction,
        payload.predicted_move_pips,
        payload.actual_move_pips,
    )


@router.post('/channel-growth', response_model=ChannelGrowthResponse)
def channel_growth(payload: ChannelGrowthRequest) -> ChannelGrowthResponse:
    return excellence_service.channel_growth(
        payload.channel_id,
        payload.posts_last_7d,
        payload.reactions_last_7d,
        payload.shares_last_7d,
    )
