from dataclasses import dataclass

import httpx

from app.core.logging import get_logger
from app.core.settings import settings

logger = get_logger(__name__)


@dataclass
class SourceResult:
    source: str
    payload: dict


class ExternalNewsService:
    timeout_seconds = 5

    @classmethod
    def fetch_with_failover(cls) -> SourceResult:
        for source_name, url in [('primary', settings.primary_news_api), ('backup', settings.backup_news_api)]:
            try:
                resp = httpx.get(url, timeout=cls.timeout_seconds)
                if resp.status_code == 200:
                    return SourceResult(source=source_name, payload=resp.json() if resp.text else {})
            except Exception as exc:
                logger.warning('news source=%s failed: %s', source_name, exc)
        return SourceResult(source='fallback-empty', payload={})
