import hashlib
import json
from datetime import datetime, timedelta, timezone

from app.core.logging import get_logger

logger = get_logger(__name__)


class AICacheService:
    """Lightweight TTL cache for AI outputs (10 minutes semantic hash window)."""

    def __init__(self, ttl_minutes: int = 10) -> None:
        self.ttl = timedelta(minutes=ttl_minutes)
        self._store: dict[str, tuple[datetime, dict]] = {}

    @staticmethod
    def _key(text: str) -> str:
        normalized = ' '.join(text.lower().split())
        return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

    def get(self, text: str) -> dict | None:
        key = self._key(text)
        payload = self._store.get(key)
        if not payload:
            return None
        created_at, data = payload
        if datetime.now(timezone.utc) - created_at > self.ttl:
            self._store.pop(key, None)
            return None
        return json.loads(json.dumps(data))

    def set(self, text: str, value: dict) -> None:
        key = self._key(text)
        self._store[key] = (datetime.now(timezone.utc), value)
        logger.info('AI cache set for key=%s', key[:8])


ai_cache_service = AICacheService(ttl_minutes=10)
