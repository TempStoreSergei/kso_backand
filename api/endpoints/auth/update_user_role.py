from fastapi import Depends, HTTPException, status

from api.DTO.endpoints.auth.update_user_role_dto import UpdateUserRoleRequestDTO, \
    UpdateUserRoleResponseDTO
from api.db.auth_repository import AuthDatabaseRepository
from api.dependencies.check_user_role import role
from api.dependencies.get_obj_db import get_auth_repo
from api.models.auth_models import User


async def update_user_role(
    update_data: UpdateUserRoleRequestDTO,
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
    _: User = Depends(role(["admin"])),
):
    user = await auth_repo.update(
        filters={"username": update_data.username}, values={"role": update_data.role}
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return UpdateUserRoleResponseDTO(id=user.id, username=user.username, role=user.role)
