import httpx

from app.core.logging import get_logger
from app.core.settings import settings

logger = get_logger(__name__)


class MonitoringService:
    @staticmethod
    def _send_admin_telegram(message: str) -> None:
        if not settings.bot_token or not settings.admin_id:
            return
        endpoint = f'https://api.telegram.org/bot{settings.bot_token}/sendMessage'
        payload = {'chat_id': settings.admin_id, 'text': message}
        with httpx.Client(timeout=3.0) as client:
            response = client.post(endpoint, json=payload)
            response.raise_for_status()

    @classmethod
    def alert_developer(cls, message: str) -> None:
        logger.error('DEVELOPER ALERT: %s', message)
        try:
            cls._send_admin_telegram(f'🚨 FinIntel alert\n{message}')
        except httpx.HTTPError as exc:
            logger.error('failed to send telegram admin alert: %s', exc)

    @classmethod
    def record_api_failure(cls, service: str, detail: str) -> None:
        msg = f'API failure service={service} detail={detail}'
        logger.error(msg)
        cls.alert_developer(msg)

    @classmethod
    def notify_ai_quota_low(cls) -> None:
        cls.alert_developer('AI API quota appears low/unavailable. Falling back to raw formatter output.')
