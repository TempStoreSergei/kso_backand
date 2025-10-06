from sqlalchemy import select
from sqlalchemy.orm import selectinload

from api.db.base_database_repository import BaseDatabaseRepository
from api.db.error_handlers import handle_db_error
from api.models.guests_models import Guest, Transaction, Service, Room


class RoomDatabaseRepository(BaseDatabaseRepository):
    model_class = Room


class GuestDatabaseRepository(BaseDatabaseRepository):
    model_class = Guest


class ServiceDatabaseRepository(BaseDatabaseRepository):
    model_class = Service


class TransactionDatabaseRepository(BaseDatabaseRepository):
    model_class = Transaction

    @handle_db_error
    async def get_all_transactions(self):
        result = await self.session.execute(
            select(self.model_class)
            .options(
                selectinload(self.model_class.guest),
                selectinload(self.model_class.services),
                selectinload(self.model_class.room),
            )
        )
        transactions = result.scalars().all()
        return transactions
