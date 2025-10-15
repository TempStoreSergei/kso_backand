from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from api.db.base_database_repository import BaseDatabaseRepository
from api.db.error_handlers import handle_db_error
from modules.hotel.models.models import Guest, Transaction, Service, RoomPrice, Fine, transaction_services, transaction_fines


class RoomPriceDatabaseRepository(BaseDatabaseRepository):
    model_class = RoomPrice


class GuestDatabaseRepository(BaseDatabaseRepository):
    model_class = Guest


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
                selectinload(self.model_class.fines),
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
            stmt = select(self.model_class).where(self.model_class.room_number == room_name)

        result = await self.session.execute(stmt)
        transactions = result.scalars().unique().all()

        # Обогащаем каждую транзакцию метаданными услуг и штрафов
        enriched_transactions = []
        for transaction in transactions:
            # Получаем метаданные услуг
            services_stmt = select(
                Service.id,
                Service.name,
                Service.price,
                Service.tax,
                transaction_services.c.count,
                transaction_services.c.duration
            ).select_from(transaction_services).join(Service).where(
                transaction_services.c.transaction_id == transaction.id
            )
            services_result = await self.session.execute(services_stmt)
            services_rows = services_result.fetchall()

            # Получаем метаданные штрафов
            fines_stmt = select(
                Fine.id,
                Fine.name,
                Fine.price,
                Fine.type,
                transaction_fines.c.count
            ).select_from(transaction_fines).join(Fine).where(
                transaction_fines.c.transaction_id == transaction.id
            )
            fines_result = await self.session.execute(fines_stmt)
            fines_rows = fines_result.fetchall()

            # Добавляем метаданные к объектам
            transaction.services_meta = services_rows
            transaction.fines_meta = fines_rows

            enriched_transactions.append(transaction)

        return enriched_transactions

    @handle_db_error
    async def add_services(self, transaction_id: int, services_meta: list[dict]):
        """Добавляет услуги к транзакции с метаданными"""
        for meta in services_meta:
            await self.session.execute(
                insert(transaction_services).values(
                    transaction_id=transaction_id,
                    service_id=meta['service'].id,
                    count=meta['count'],
                    duration=meta['duration']
                )
            )

    @handle_db_error
    async def add_fines(self, transaction_id: int, fines_meta: list[dict]):
        """Добавляет штрафы к транзакции с метаданными"""
        for meta in fines_meta:
            await self.session.execute(
                insert(transaction_fines).values(
                    transaction_id=transaction_id,
                    fine_id=meta['fine'].id,
                    count=meta['count']
                )
            )

    @handle_db_error
    async def update_transaction(
            self,
            transaction_id: int,
            guest: dict | None,
            room: dict | None,
    ):
        stmt = (
            select(self.model_class).where(self.model_class.id == transaction_id)
            .options(
                selectinload(self.model_class.guest),
            )
        )
        result = await self.session.execute(stmt)
        transaction = result.scalar_one_or_none()

        if transaction and guest:
            first_name = guest['first_name']
            last_name = guest['last_name']
            surname = guest['surname']
            if first_name:
                transaction.guest.first_name = first_name
            if last_name:
                transaction.guest.last_name = last_name
            if surname:
                transaction.guest.surname = surname

        if transaction and room:
            number = room['number']
            room_type = room['type']
            building = room['building']
            if number:
                transaction.room_number = number
            if room_type:
                transaction.room_type = room_type
            if building:
                transaction.room_building = building

        return transaction
