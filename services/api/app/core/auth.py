from fastapi import HTTPException, Request


ALLOWED_ADMIN_HOSTS = {'127.0.0.1', 'localhost'}


def require_admin(request: Request) -> str:
    host = request.client.host if request.client else ''
    if host not in ALLOWED_ADMIN_HOSTS:
        raise HTTPException(status_code=403, detail='admin access denied')
    return host
