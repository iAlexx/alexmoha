from fastapi import APIRouter

from app.schemas.advanced_analysis import (
    DivergenceAlertRequest,
    DivergenceAlertResponse,
    HeatmapResponse,
    InstantBacktestRequest,
    InstantBacktestResponse,
    LiquidityLevelRequest,
    LiquidityLevelResponse,
)
from app.services.advanced_analysis import AdvancedAnalysisService

router = APIRouter()


@router.get('/heatmap', response_model=HeatmapResponse)
def smart_heatmap() -> HeatmapResponse:
    strongest, weakest = AdvancedAnalysisService.smart_heatmap()
    return HeatmapResponse(strongest=strongest, weakest=weakest)


@router.post('/divergence', response_model=DivergenceAlertResponse)
def divergence(payload: DivergenceAlertRequest) -> DivergenceAlertResponse:
    div, msg = AdvancedAnalysisService.divergence(payload.symbol, payload.news_impact_score, payload.price_move_pct)
    return DivergenceAlertResponse(divergence=div, message=msg)


@router.post('/instant-backtest', response_model=InstantBacktestResponse)
def instant_backtest(payload: InstantBacktestRequest) -> InstantBacktestResponse:
    url, move = AdvancedAnalysisService.instant_backtest(payload.symbol, payload.event_type)
    return InstantBacktestResponse(chart_hint_url=url, median_move_pips=move)


@router.post('/liquidity-level', response_model=LiquidityLevelResponse)
def liquidity_level(payload: LiquidityLevelRequest) -> LiquidityLevelResponse:
    near, dist, msg = AdvancedAnalysisService.liquidity_level(payload.symbol, payload.current_price, payload.major_level)
    return LiquidityLevelResponse(near_level=near, distance_pct=dist, message=msg)
