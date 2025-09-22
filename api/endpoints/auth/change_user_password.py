from fastapi import Depends, HTTPException

from api.DTO.endpoints.auth.change_user_password_dto import ChangeUserPasswordRequestDTO, \
    ChangeUserPasswordResponseDTO
from api.dependencies.get_obj_db import get_auth_repo
from api.db.auth_repository import AuthDatabaseRepository
from api.dependencies.get_current_user import get_current_user
from api.models.auth_models import User


async def change_user_password(
    data: ChangeUserPasswordRequestDTO,
    user: User = Depends(get_current_user),
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
) -> ChangeUserPasswordResponseDTO:
    if user.user_password != data.old_password:
        raise HTTPException(400, 'Старый и новый пароли не совпадают')
    await auth_repo.change_user_password(user.id, data.new_password)
    return ChangeUserPasswordResponseDTO(detail='Пароль пользователя изменен успешно')
