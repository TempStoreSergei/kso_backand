from uuid import UUID

from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload
from fastapi import HTTPException

from api.db.base_database_repository import BaseDatabaseRepository
from api.db.error_handlers import handle_db_error
from api.models.auth_models import User
from api.utils.auth.devpass import hash_password, verify_password


class AuthDatabaseRepository(BaseDatabaseRepository):
    model_class = User

    async def register_user(self, username: str, password: str):
        existing_user = await self.get(username=username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Пользователь с таким именем уже существует")
        hashed = hash_password(password)
        user = await self.create(username=username, password=hashed)
        return user

    # async def get_user_by_username(self, username: str) -> User:
    #     return await self.get(username=username)
    #
    # async def update_password(self, username: str, password: str):
    #     return await self.update(filters={"username": username}, values={"password": password})
    #
    # async def update_role(self, username: str, role: str):
    #     return await self.update(filters={"username": username}, values={"role": role})
    #
    # async def delete_user(self, username: str):
    #     return await self.delete(username=username)

    async def authenticate_user(self, username: str, password: str):
        user = await self.get(username=username)
        if user and verify_password(password, user.password):
            return user
        return None
