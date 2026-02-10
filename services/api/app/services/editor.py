from app.core.settings import settings
from app.schemas.editor import Tone
from app.services.cache import ai_cache_service
from app.utils.formatter import format_news_with_ai


class AutoEditorService:
    _admin_tone: Tone = 'fast_news'

    @classmethod
    def set_tone(cls, tone: Tone) -> Tone:
        cls._admin_tone = tone
        return cls._admin_tone

    @classmethod
    def get_tone(cls) -> Tone:
        return cls._admin_tone

    @staticmethod
    def llm_provider() -> str:
        if not settings.ai_token:
            return 'fallback'
        return settings.llm_provider

    @staticmethod
    def system_prompt() -> str:
        return settings.llm_system_prompt

    @classmethod
    def format_news(cls, raw_text: str, source: str, lang: str, tone: Tone | None = None) -> tuple[str, str | None]:
        cache_key = f'{source}:{lang}:{raw_text}'
        cached = ai_cache_service.get(cache_key)
        if cached:
            return cached.get('formatted_markdown', ''), cached.get('translated_ar')

        selected = tone or cls._admin_tone
        formatted_body = format_news_with_ai(raw_text)
        prefix = '⚡️' if selected in {'aggressive', 'fast_news'} else '🧠'
        formatted = (
            f"{prefix} *{source.upper()}*\\n\\n{formatted_body}\\n\\n"
            f"_Style: {selected} | Provider: {cls.llm_provider()}_"
        )
        translated = f'📌 ترجمة مالية سريعة:\n{formatted_body}' if lang == 'ar' else None

        ai_cache_service.set(cache_key, {'formatted_markdown': formatted, 'translated_ar': translated})
        return formatted, translated

    @staticmethod
    def summarize(text: str, max_points: int) -> list[str]:
        parts = [p.strip() for p in text.replace('\n', '. ').split('.') if p.strip()]
        return [f'• {p}' for p in parts[:max_points]] or ['• No key points extracted']
