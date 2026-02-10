from fastapi import APIRouter

from app.schemas.alerts import EconomicCalendarAlertRequest, EconomicCalendarAlertResponse

router = APIRouter()


@router.post("/economic-calendar", response_model=EconomicCalendarAlertResponse)
def economic_calendar_alert(payload: EconomicCalendarAlertRequest) -> EconomicCalendarAlertResponse:
    actual_text = payload.actual if payload.actual else "Pending"
    actual_text_ar = payload.actual if payload.actual else "قيد الانتظار"
    prefix = f"T-{payload.t_minus_minutes}m" if payload.t_minus_minutes else "Release"
    prefix_ar = f"قبل {payload.t_minus_minutes} دقيقة" if payload.t_minus_minutes else "وقت الإصدار"

    message_en = (
        f"[{prefix}] {payload.currency} | {payload.event} | "
        f"Prev: {payload.previous} | Forecast: {payload.forecast} | Actual: {actual_text}"
    )
    message_ar = (
        f"[{prefix_ar}] {payload.currency} | {payload.event} | "
        f"السابق: {payload.previous} | المتوقع: {payload.forecast} | الفعلي: {actual_text_ar}"
    )

    priority = "critical" if payload.actual and payload.actual != payload.forecast else "high"

    return EconomicCalendarAlertResponse(message_ar=message_ar, message_en=message_en, priority=priority)
