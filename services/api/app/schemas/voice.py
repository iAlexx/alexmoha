from pydantic import BaseModel


class VoiceQueryRequest(BaseModel):
    user_id: str
    audio_url: str
    lang: str = 'ar'


class VoiceQueryResponse(BaseModel):
    transcript: str
    answer: str
    confidence: float
