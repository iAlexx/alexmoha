from fastapi import APIRouter

from app.schemas.intelligence import (
    BacktestNewsRequest,
    BacktestNewsResponse,
    FakeNewsCheckRequest,
    FakeNewsCheckResponse,
    GapDetectorRequest,
    GapDetectorResponse,
    NoiseFilterRequest,
    NoiseFilterResponse,
    SessionMasterRequest,
    SessionMasterResponse,
)
from app.services.intelligence import ProactiveIntelligenceService, VipIntelligenceService

router = APIRouter()


@router.post('/session-master', response_model=SessionMasterResponse)
def session_master(payload: SessionMasterRequest) -> SessionMasterResponse:
    return ProactiveIntelligenceService.session_master(payload.session)


@router.post('/gap-detector', response_model=GapDetectorResponse)
def gap_detector(payload: GapDetectorRequest) -> GapDetectorResponse:
    return ProactiveIntelligenceService.gap_detector(payload.symbol, payload.friday_close, payload.monday_open)


@router.post('/noise-filter', response_model=NoiseFilterResponse)
def noise_filter(payload: NoiseFilterRequest) -> NoiseFilterResponse:
    if payload.high_impact_mode and payload.incoming_impact_score <= 6:
        return NoiseFilterResponse(allow_alert=False, policy='suppressed_by_high_impact_filter')
    return NoiseFilterResponse(allow_alert=True, policy='normal_delivery')


@router.post('/vip/backtest-news', response_model=BacktestNewsResponse)
def backtest_news(payload: BacktestNewsRequest) -> BacktestNewsResponse:
    return VipIntelligenceService.backtest_news(payload.asset, payload.event_type, payload.lookback_days)


@router.post('/vip/fake-news-check', response_model=FakeNewsCheckResponse)
def fake_news_check(payload: FakeNewsCheckRequest) -> FakeNewsCheckResponse:
    return VipIntelligenceService.fake_news_detection(payload.trusted_sources_matched)
