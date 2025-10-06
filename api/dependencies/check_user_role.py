from fastapi import Depends, HTTPException

from api.dependencies.get_current_user import get_current_user
from api.models.auth_models import User


def role(allowed_roles: list[str]):
    def role_validator(current_user: User = Depends(get_current_user)):
        if not any(r in current_user.role for r in allowed_roles):
            raise HTTPException(status_code=403, detail="Acсess dined")
        return current_user
    return role_validator
