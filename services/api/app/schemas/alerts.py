from typing import Literal

from pydantic import BaseModel, Field


class EconomicCalendarAlertRequest(BaseModel):
    event: str
    currency: str
    previous: str
    forecast: str
    actual: str | None = None
    t_minus_minutes: Literal[30, 15, 5] | None = Field(default=None)


class EconomicCalendarAlertResponse(BaseModel):
    message_ar: str
    message_en: str
    priority: Literal["normal", "high", "critical"]
