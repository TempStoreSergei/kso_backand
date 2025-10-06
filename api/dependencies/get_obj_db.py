from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_async_session
from api.db.auth_repository import AuthDatabaseRepository
from api.db.guest_repository import GuestDatabaseRepository, TransactionDatabaseRepository, \
    ServiceDatabaseRepository, RoomDatabaseRepository


async def get_room_repo(session: AsyncSession = Depends(get_async_session)):
    yield RoomDatabaseRepository(session)


async def get_auth_repo(session: AsyncSession = Depends(get_async_session)):
    yield AuthDatabaseRepository(session)


async def get_guest_repo(session: AsyncSession = Depends(get_async_session)):
    yield GuestDatabaseRepository(session)


async def get_service_repo(session: AsyncSession = Depends(get_async_session)):
    yield ServiceDatabaseRepository(session)


async def get_transaction_repo(session: AsyncSession = Depends(get_async_session)):
    yield TransactionDatabaseRepository(session)
