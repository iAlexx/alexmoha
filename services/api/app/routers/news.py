from fastapi import APIRouter

from app.schemas.news import AskNewsRequest, AskNewsResponse, NewsIngestRequest, NewsIngestResponse
from app.services.ai_engine import AIEngine

router = APIRouter()


@router.post("/ingest", response_model=NewsIngestResponse)
def ingest_news(payload: NewsIngestRequest) -> NewsIngestResponse:
    result = AIEngine.analyze(payload.title, payload.body)

    return NewsIngestResponse(
        accepted=True,
        dedup_group_id=result.dedup_group_id,
        sentiment=result.sentiment,
        impact_score=result.impact_score,
        normalized_title_ar=payload.title if payload.lang == "ar" else None,
        normalized_title_en=payload.title if payload.lang == "en" else None,
    )


@router.post("/ask", response_model=AskNewsResponse)
def ask_news(payload: AskNewsRequest) -> AskNewsResponse:
    answer, confidence = AIEngine.answer_question(payload.question, payload.lang)
    return AskNewsResponse(answer=answer, confidence=confidence)
