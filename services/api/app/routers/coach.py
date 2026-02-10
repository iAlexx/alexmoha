from fastapi import APIRouter

from app.schemas.coach import (
    MonthlyPerformanceRequest,
    MonthlyPerformanceResponse,
    TradingNoteRequest,
    TradingNoteResponse,
)
from app.services.coach import coach_service

router = APIRouter()


@router.post('/note', response_model=TradingNoteResponse)
def add_note(payload: TradingNoteRequest) -> TradingNoteResponse:
    accepted, total = coach_service.add_note(payload.user_id, payload.tier, payload.note)
    return TradingNoteResponse(accepted=accepted, total_notes=total)


@router.post('/monthly-report', response_model=MonthlyPerformanceResponse)
def monthly_report(payload: MonthlyPerformanceRequest) -> MonthlyPerformanceResponse:
    s, m, p = coach_service.monthly_report(payload.user_id, payload.month)
    return MonthlyPerformanceResponse(strengths=s, mistakes=m, improvement_plan=p)
