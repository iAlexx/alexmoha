from typing import Literal

from pydantic import BaseModel


Tone = Literal['aggressive', 'conservative', 'educational', 'fast_news']


class AutoEditRequest(BaseModel):
    raw_text: str
    source: str
    lang: Literal['ar', 'en'] = 'ar'
    tone: Tone = 'fast_news'


class AutoEditResponse(BaseModel):
    formatted_markdown: str
    translated_ar: str | None = None


class SummarizeRequest(BaseModel):
    text: str
    max_points: int = 5


class SummarizeResponse(BaseModel):
    bullets: list[str]


class AdminToneRequest(BaseModel):
    tone: Tone


class AdminToneResponse(BaseModel):
    tone: Tone
    updated: bool
