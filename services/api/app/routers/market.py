from fastapi import APIRouter

from app.schemas.market import (
    CorrelationRadarRequest,
    CorrelationRadarResponse,
    WhaleDetectionRequest,
    WhaleDetectionResponse,
)
from app.services.market_intelligence import MarketIntelligenceService

router = APIRouter()


@router.post('/correlation-radar', response_model=CorrelationRadarResponse)
def correlation_radar(payload: CorrelationRadarRequest) -> CorrelationRadarResponse:
    opportunities = MarketIntelligenceService.correlation_radar(payload.trigger_symbol, payload.trigger_move_pct)
    return CorrelationRadarResponse(trigger_symbol=payload.trigger_symbol, opportunities=opportunities)


@router.post('/whale-detector', response_model=WhaleDetectionResponse)
def whale_detector(payload: WhaleDetectionRequest) -> WhaleDetectionResponse:
    return MarketIntelligenceService.whale_detector(payload.asset, payload.transfer_usd, payload.price_spike_pct)
