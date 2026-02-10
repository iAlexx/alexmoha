from fastapi import APIRouter

from app.schemas.editor import (
    AdminToneRequest,
    AdminToneResponse,
    AutoEditRequest,
    AutoEditResponse,
    SummarizeRequest,
    SummarizeResponse,
)
from app.services.editor import AutoEditorService

router = APIRouter()


@router.post('/auto-edit', response_model=AutoEditResponse)
def auto_edit(payload: AutoEditRequest) -> AutoEditResponse:
    formatted, translated = AutoEditorService.format_news(payload.raw_text, payload.source, payload.lang, payload.tone)
    return AutoEditResponse(formatted_markdown=formatted, translated_ar=translated)


@router.post('/summarize', response_model=SummarizeResponse)
def summarize(payload: SummarizeRequest) -> SummarizeResponse:
    return SummarizeResponse(bullets=AutoEditorService.summarize(payload.text, payload.max_points))


@router.put('/admin-tone', response_model=AdminToneResponse)
def admin_tone(payload: AdminToneRequest) -> AdminToneResponse:
    tone = AutoEditorService.set_tone(payload.tone)
    return AdminToneResponse(tone=tone, updated=True)
