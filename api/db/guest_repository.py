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
    async def get_all_transactions(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        surname: str | None = None,
        room_name: str | None = None,
    ):
        stmt = (
            select(self.model_class)
            .options(
                selectinload(self.model_class.guest),
                selectinload(self.model_class.services),
                selectinload(self.model_class.room),
            )
        )

        # --- Фильтр по гостю ---
        if any([first_name, last_name, surname]):
            stmt = stmt.join(self.model_class.guest)

            if first_name:
                stmt = stmt.where(Guest.first_name.ilike(f"%{first_name}%"))
            if last_name:
                stmt = stmt.where(Guest.last_name.ilike(f"%{last_name}%"))
            if surname:
                stmt = stmt.where(Guest.surname.ilike(f"%{surname}%"))

        # --- Фильтр по названию комнаты ---
        if room_name:
            stmt = stmt.join(self.model_class.room)
            stmt = stmt.where(Room.name.ilike(f"%{room_name}%"))

        result = await self.session.execute(stmt)
        transactions = result.scalars().unique().all()
        return transactions
