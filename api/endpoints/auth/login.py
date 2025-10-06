from fastapi import Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm

from api.DTO.endpoints.auth.login_dto import LoginResponseDTO
from api.db.auth_repository import AuthDatabaseRepository
from api.dependencies.get_obj_db import get_auth_repo
from api.utils.auth.create_jwt import create_jwt_token, create_refresh_token
from api.utils.auth.devpass import pwd_context


async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
):
    user = await auth_repo.get(username=form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_jwt_token({"sub": user.username})
    refresh_token = create_refresh_token({"sub": user.username})

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="strict",
        max_age=60 * 15  # 15 минут
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=False,
        secure=True,
        samesite="strict",
        max_age=3600 * 24 * 7  # 7 дней
    )

    return LoginResponseDTO(detail="logged in")
