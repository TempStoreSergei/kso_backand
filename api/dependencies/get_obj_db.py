from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_async_session
from api.db.auth_repository import AuthDatabaseRepository, CookieDatabaseRepository


async def get_auth_repo(session: AsyncSession = Depends(get_async_session)):
    yield AuthDatabaseRepository(session)

async def get_cookie_repo(session: AsyncSession = Depends(get_async_session)):
    yield CookieDatabaseRepository(session)
