from fastapi import APIRouter

from app.schemas.digest import DailyDigestRequest, DailyDigestResponse
from app.services.digest import DailyDigestService

router = APIRouter()


@router.post('/daily', response_model=DailyDigestResponse)
def daily_digest(payload: DailyDigestRequest) -> DailyDigestResponse:
    digest, watch = DailyDigestService.build_digest(payload.date, payload.headlines)
    return DailyDigestResponse(digest_markdown=digest, watchlist_tomorrow=watch)
