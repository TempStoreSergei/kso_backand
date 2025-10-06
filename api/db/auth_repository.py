from fastapi import HTTPException

from api.db.base_database_repository import BaseDatabaseRepository
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

    async def authenticate_user(self, username: str, password: str):
        user = await self.get(username=username)
        if user and verify_password(password, user.password):
            return user
        return None
