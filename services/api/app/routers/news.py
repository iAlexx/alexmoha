from fastapi import APIRouter, HTTPException, Request

from app.core.runtime_state import runtime_state
from app.schemas.news import AskNewsRequest, AskNewsResponse, NewsIngestRequest, NewsIngestResponse
from app.services.ai_engine import AIEngine
from app.services.anti_spam import anti_spam_service

router = APIRouter()


@router.post('/ingest', response_model=NewsIngestResponse)
def ingest_news(payload: NewsIngestRequest, request: Request) -> NewsIngestResponse:
    if runtime_state.maintenance_mode or runtime_state.emergency_pause:
        raise HTTPException(status_code=503, detail='service paused by admin')

    actor = request.client.host if request.client else 'unknown'
    if not anti_spam_service.allow(f'ingest:{actor}'):
        raise HTTPException(status_code=429, detail='too many requests')

    result = AIEngine.analyze(payload.title, payload.body)

    return NewsIngestResponse(
        accepted=True,
        dedup_group_id=result.dedup_group_id,
        sentiment=result.sentiment,
        impact_score=result.impact_score,
        normalized_title_ar=payload.title if payload.lang == 'ar' else None,
        normalized_title_en=payload.title if payload.lang == 'en' else None,
    )


@router.post('/ask', response_model=AskNewsResponse)
def ask_news(payload: AskNewsRequest, request: Request) -> AskNewsResponse:
    actor = request.client.host if request.client else 'unknown'
    if not anti_spam_service.allow(f'ask:{actor}'):
        raise HTTPException(status_code=429, detail='too many requests')

    answer, confidence = AIEngine.answer_question(payload.question, payload.lang)
    return AskNewsResponse(answer=answer, confidence=confidence)
