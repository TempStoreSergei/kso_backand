from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from api.configs.app import security
from api.dependencies.get_obj_db import get_cookie_repo
from api.db.auth_repository import CookieDatabaseRepository


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    cookie_repo: CookieDatabaseRepository = Depends(get_cookie_repo),
):
    cookie = await cookie_repo.get_cookie_by_token(credentials.credentials)
    if not cookie:
        raise HTTPException(401, "Некорректные куки")
    return cookie.user
