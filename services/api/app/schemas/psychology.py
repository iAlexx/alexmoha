from pydantic import BaseModel


class PsychologicalAlertRequest(BaseModel):
    symbol: str
    volatility_index: float


class PsychologicalAlertResponse(BaseModel):
    send_calm_alert: bool
    message: str
