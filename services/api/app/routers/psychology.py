from fastapi import APIRouter

from app.schemas.psychology import PsychologicalAlertRequest, PsychologicalAlertResponse
from app.services.psychology import PsychologyService

router = APIRouter()


@router.post('/calm-alert', response_model=PsychologicalAlertResponse)
def calm_alert(payload: PsychologicalAlertRequest) -> PsychologicalAlertResponse:
    send, msg = PsychologyService.calm_alert(payload.symbol, payload.volatility_index)
    return PsychologicalAlertResponse(send_calm_alert=send, message=msg)
