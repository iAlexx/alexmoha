from typing import Annotated

from fastapi import APIRouter, Depends

from app.core.auth import require_admin
from app.core.runtime_state import runtime_state
from app.core.settings import settings
from app.schemas.admin import AdminDashboardResponse, RuntimeFlagsResponse, RuntimeFlagsUpdateRequest

router = APIRouter()


@router.get('/dashboard', response_model=AdminDashboardResponse)
def admin_dashboard(_: Annotated[str, Depends(require_admin)]) -> AdminDashboardResponse:
    return AdminDashboardResponse(
        admin_id='local-admin',
        webapp_url=settings.telegram_webapp_url,
        commands=['broadcast', 'vip_codes', 'stats', 'maintenance_mode', 'emergency_pause'],
    )


@router.get('/runtime-flags', response_model=RuntimeFlagsResponse)
def get_runtime_flags(_: Annotated[str, Depends(require_admin)]) -> RuntimeFlagsResponse:
    return RuntimeFlagsResponse(
        maintenance_mode=runtime_state.maintenance_mode,
        emergency_pause=runtime_state.emergency_pause,
        updated_at=runtime_state.updated_at,
    )


@router.patch('/runtime-flags', response_model=RuntimeFlagsResponse)
def update_runtime_flags(
    payload: RuntimeFlagsUpdateRequest,
    _: Annotated[str, Depends(require_admin)],
) -> RuntimeFlagsResponse:
    runtime_state.set_flags(payload.maintenance_mode, payload.emergency_pause)
    return RuntimeFlagsResponse(
        maintenance_mode=runtime_state.maintenance_mode,
        emergency_pause=runtime_state.emergency_pause,
        updated_at=runtime_state.updated_at,
    )
