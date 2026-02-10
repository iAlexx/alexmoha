from fastapi import APIRouter

from app.schemas.infra import FailoverFetchResponse, SystemHealthResponse
from app.services.external_sources import ExternalNewsService
from app.services.monitoring import MonitoringService

router = APIRouter()


@router.get('/news-failover-test', response_model=FailoverFetchResponse)
def news_failover_test() -> FailoverFetchResponse:
    result = ExternalNewsService.fetch_with_failover()
    if result.source == 'fallback-empty':
        MonitoringService.alert_developer('Both primary and backup news sources unavailable.')
    return FailoverFetchResponse(source_used=result.source, payload_size=len(result.payload))


@router.get('/system-health', response_model=SystemHealthResponse)
def system_health() -> SystemHealthResponse:
    # Placeholder active checks until DB/Redis clients are integrated.
    db = 'ok'
    redis = 'ok'
    ai_api = 'ok'
    overall = 'ok'
    if 'down' in {db, redis, ai_api}:
        overall = 'degraded'
        MonitoringService.alert_developer('Critical service degraded (db/redis/ai_api).')
    return SystemHealthResponse(database=db, redis=redis, ai_api=ai_api, overall=overall)
