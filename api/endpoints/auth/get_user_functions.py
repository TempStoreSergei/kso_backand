from fastapi import Depends

from api.DTO.endpoints.auth.get_user_functioins_dto import GetUserFunctionsResponseDTO
from api.db.auth_repository import AuthDatabaseRepository
from api.dependencies.get_current_user import get_current_user
from api.dependencies.get_obj_db import get_auth_repo
from api.models.auth_models import User


async def get_user_functions(
    user: User = Depends(get_current_user),
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
):
    user_functions = await auth_repo.get_user_functions(user.id)
    func_names = []
    for func in user_functions:
        func_names.append(func)
    return GetUserFunctionsResponseDTO(functions=func_names)
