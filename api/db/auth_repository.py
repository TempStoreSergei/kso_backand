from uuid import UUID

from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

from api.db.base_database_repository import BaseDatabaseRepository
from api.db.error_handlers import handle_db_error
from api.models.auth_models import User, Cookie, UserFunctionsMap, TerminalFunctions


class AuthDatabaseRepository(BaseDatabaseRepository):
    """Репозиторий для работы с """
    model_class = User

    @handle_db_error
    async def login(self, username: str, password: str):
        query = select(self.model_class).where(
            and_(self.model_class.user_name == username, self.model_class.user_password == password)
        )
        result = await self.session.execute(query)
        user = result.scalar_one_or_none()
        return user

    @handle_db_error
    async def change_user_password(self, user_id: UUID, new_password: str):
        user = await self.session.get(self.model_class, user_id)
        user.user_password = new_password
        await self.session.commit()

    @handle_db_error
    async def get_user_functions(self, user_id: UUID):
        query = (select(TerminalFunctions.function_name)
                 .join(UserFunctionsMap,TerminalFunctions.id == UserFunctionsMap.terminal_function_id)
                 .where(UserFunctionsMap.user_id == user_id))
        result = await self.session.execute(query)
        functions = result.scalars().all()
        if not functions:
            return None
        return functions


class CookieDatabaseRepository(BaseDatabaseRepository):
    """Репозиторий для работы с """
    model_class = Cookie

    @handle_db_error
    async def get_cookie_by_token(self, token):
        query = select(Cookie).where(Cookie.token == token).options(selectinload(Cookie.user))
        result = await self.session.execute(query)
        cookie = result.scalar_one_or_none()
        if not cookie:
            return False
        return cookie
