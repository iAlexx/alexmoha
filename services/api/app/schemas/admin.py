from datetime import datetime

from pydantic import BaseModel


class RuntimeFlagsResponse(BaseModel):
    maintenance_mode: bool
    emergency_pause: bool
    updated_at: datetime


class RuntimeFlagsUpdateRequest(BaseModel):
    maintenance_mode: bool | None = None
    emergency_pause: bool | None = None
