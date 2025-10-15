from fastapi import Depends

from api.DTO.auth.register_dto import RegisterResponseDTO, RegisterRequestDTO
from api.db.auth_repository import AuthDatabaseRepository
from api.dependencies.get_obj_db import get_auth_repo


async def register(
    register_data: RegisterRequestDTO,
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
):
    user = await auth_repo.register_user(register_data.name, register_data.password)
    return RegisterResponseDTO(id=user.id, username=user.username, role=user.role)
