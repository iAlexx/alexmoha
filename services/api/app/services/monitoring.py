from app.core.logging import get_logger

logger = get_logger(__name__)


class MonitoringService:
    @staticmethod
    def alert_developer(message: str) -> None:
        logger.error('DEVELOPER ALERT: %s', message)

    @staticmethod
    def record_api_failure(service: str, detail: str) -> None:
        logger.error('API failure service=%s detail=%s', service, detail)
