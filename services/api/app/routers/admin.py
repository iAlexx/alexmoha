from fastapi import APIRouter

from app.core.runtime_state import runtime_state
from app.schemas.admin import RuntimeFlagsResponse, RuntimeFlagsUpdateRequest

router = APIRouter()


@router.get('/runtime-flags', response_model=RuntimeFlagsResponse)
def get_runtime_flags() -> RuntimeFlagsResponse:
    return RuntimeFlagsResponse(
        maintenance_mode=runtime_state.maintenance_mode,
        emergency_pause=runtime_state.emergency_pause,
        updated_at=runtime_state.updated_at,
    )


@router.patch('/runtime-flags', response_model=RuntimeFlagsResponse)
def update_runtime_flags(payload: RuntimeFlagsUpdateRequest) -> RuntimeFlagsResponse:
    runtime_state.set_flags(payload.maintenance_mode, payload.emergency_pause)
    return RuntimeFlagsResponse(
        maintenance_mode=runtime_state.maintenance_mode,
        emergency_pause=runtime_state.emergency_pause,
        updated_at=runtime_state.updated_at,
    )
