import json

import httpx

from app.core.logging import get_logger
from app.core.settings import settings
from app.services.monitoring import MonitoringService

logger = get_logger(__name__)


def _openai_format(raw_news: str, timeout_s: float) -> str | None:
    if not settings.ai_token:
        return None

    payload = {
        'model': 'gpt-4o-mini',
        'messages': [
            {'role': 'system', 'content': settings.llm_system_prompt},
            {
                'role': 'user',
                'content': (
                    'Rewrite this raw financial news as catchy/professional markdown with emojis, '\
                    'bullet points, and a 1-line sentiment read.\\n\\n'
                    f'RAW NEWS:\\n{raw_news}'
                ),
            },
        ],
        'temperature': 0.2,
    }
    headers = {'Authorization': f'Bearer {settings.ai_token}'}
    with httpx.Client(timeout=timeout_s) as client:
        response = client.post('https://api.openai.com/v1/chat/completions', json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content'].strip()


def _gemini_format(raw_news: str, timeout_s: float) -> str | None:
    if not settings.ai_token:
        return None

    endpoint = (
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent'
        f'?key={settings.ai_token}'
    )
    payload = {
        'system_instruction': {'parts': [{'text': settings.llm_system_prompt}]},
        'contents': [
            {
                'parts': [
                    {
                        'text': (
                            'Rewrite this raw financial news as catchy/professional markdown with emojis, '
                            'bullet points, and one-line sentiment.\\n\\n'
                            f'RAW NEWS:\\n{raw_news}'
                        )
                    }
                ]
            }
        ],
    }
    with httpx.Client(timeout=timeout_s) as client:
        response = client.post(endpoint, json=payload)
        response.raise_for_status()
        data = response.json()
        candidates = data.get('candidates', [])
        if not candidates:
            return None
        parts = candidates[0].get('content', {}).get('parts', [])
        merged = ' '.join(p.get('text', '') for p in parts if p.get('text'))
        return merged.strip() or None


def format_news_with_ai(raw_news: str, timeout_s: float = 4.0) -> str:
    """Format financial news using configured AI provider; fallback to raw text on failure/timeout."""
    provider = settings.llm_provider
    try:
        if provider == 'gemini':
            formatted = _gemini_format(raw_news, timeout_s)
        else:
            formatted = _openai_format(raw_news, timeout_s)

        if formatted:
            return formatted
    except (httpx.HTTPError, KeyError, IndexError, ValueError, json.JSONDecodeError) as exc:
        logger.warning('formatter provider=%s failed: %s', provider, exc)
        if isinstance(exc, httpx.HTTPStatusError) and exc.response.status_code in {401, 402, 429}:
            MonitoringService.notify_ai_quota_low()

    return raw_news
