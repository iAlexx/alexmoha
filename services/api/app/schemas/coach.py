from pydantic import BaseModel


class TradingNoteRequest(BaseModel):
    user_id: str
    tier: str
    note: str


class TradingNoteResponse(BaseModel):
    accepted: bool
    total_notes: int


class MonthlyPerformanceRequest(BaseModel):
    user_id: str
    month: str


class MonthlyPerformanceResponse(BaseModel):
    strengths: list[str]
    mistakes: list[str]
    improvement_plan: list[str]
