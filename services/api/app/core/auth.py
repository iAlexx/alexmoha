from fastapi import Header, HTTPException

from app.core.settings import settings


def require_admin(x_admin_id: str | None = Header(default=None)) -> str:
    if not settings.admin_id:
        raise HTTPException(status_code=503, detail='ADMIN_ID is not configured')
    if x_admin_id != settings.admin_id:
        raise HTTPException(status_code=403, detail='admin access denied')
    return x_admin_id
