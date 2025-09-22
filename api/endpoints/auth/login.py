from secrets import token_hex

from fastapi import Depends, HTTPException

from api.DTO.endpoints.auth.login_dto import LoginRequestDTO, LoginResponseDTO
from api.dependencies.get_obj_db import get_auth_repo, get_cookie_repo
from api.db.auth_repository import AuthDatabaseRepository, CookieDatabaseRepository
from api.configs.loggers import logger


async def login(
    login_data: LoginRequestDTO,
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
    cookie_repo: CookieDatabaseRepository = Depends(get_cookie_repo),
) -> LoginResponseDTO:
    user = await auth_repo.login(login_data.username, login_data.password)
    if not user:
        raise HTTPException(401, 'Неверные логин или пароль')

    token = token_hex(16)
    await cookie_repo.create({'user_id': user.id, 'token': token})
    logger.info(f"Пользователь {user.user_name} авторизован успешно")
    return LoginResponseDTO(access_token=token)
