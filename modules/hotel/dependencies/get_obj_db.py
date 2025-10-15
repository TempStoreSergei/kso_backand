from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.configs.database import get_async_session
from modules.hotel.db.transactions_repository import GuestDatabaseRepository, TransactionDatabaseRepository, \
    RoomPriceDatabaseRepository
from modules.hotel.db.services_repository import ServiceDatabaseRepository
from modules.hotel.db.fines_repository import FineDatabaseRepository


async def get_room_price_repo(session: AsyncSession = Depends(get_async_session)):
    yield RoomPriceDatabaseRepository(session)


async def get_guest_repo(session: AsyncSession = Depends(get_async_session)):
    yield GuestDatabaseRepository(session)


async def get_service_repo(session: AsyncSession = Depends(get_async_session)):
    yield ServiceDatabaseRepository(session)


async def get_fine_repo(session: AsyncSession = Depends(get_async_session)):
    yield FineDatabaseRepository(session)


async def get_transaction_repo(session: AsyncSession = Depends(get_async_session)):
    yield TransactionDatabaseRepository(session)
