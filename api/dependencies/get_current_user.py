from fastapi import Depends, HTTPException, Request

from api.dependencies.get_obj_db import get_auth_repo
from api.db.auth_repository import AuthDatabaseRepository
from api.utils.auth.create_jwt import verify_jwt_token


async def get_current_user(
    request: Request,
    auth_repo: AuthDatabaseRepository = Depends(get_auth_repo),
):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    decoded_data = verify_jwt_token(token)
    if not decoded_data:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = await auth_repo.get(username=decoded_data["sub"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
