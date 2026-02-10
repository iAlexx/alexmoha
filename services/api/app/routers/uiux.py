from fastapi import APIRouter

from app.schemas.uiux import InlineNewsControlsRequest, InlineNewsControlsResponse
from app.services.uiux import UIUXService

router = APIRouter()


@router.post('/inline-controls', response_model=InlineNewsControlsResponse)
def inline_controls(payload: InlineNewsControlsRequest) -> InlineNewsControlsResponse:
    return InlineNewsControlsResponse(buttons=UIUXService.inline_controls(payload.news_id))
