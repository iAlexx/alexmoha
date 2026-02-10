from fastapi import APIRouter

from app.schemas.voice import VoiceQueryRequest, VoiceQueryResponse
from app.services.voice import VoiceService

router = APIRouter()


@router.post('/ask', response_model=VoiceQueryResponse)
def voice_ask(payload: VoiceQueryRequest) -> VoiceQueryResponse:
    transcript, conf = VoiceService.transcribe(payload.audio_url, payload.lang)
    answer, _ = VoiceService.answer_from_voice(transcript, payload.lang)
    return VoiceQueryResponse(transcript=transcript, answer=answer, confidence=conf)
