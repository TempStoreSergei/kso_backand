from fastapi import Depends, HTTPException, status

from api.db.auth_repository import AuthDatabaseRepository
from api.dependencies.check_user_role import role
from api.dependencies.get_obj_db import get_auth_repo
from api.models.auth_models import User


async def delete_user(
    username: str,
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
    _: User = Depends(role(["admin"])),
):
    user_deleted = await auth_repo.delete(username=username)
    if not user_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User '{username}' not found",
        )
