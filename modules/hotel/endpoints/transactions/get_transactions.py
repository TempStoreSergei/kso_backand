from fastapi import Depends, Query

from modules.hotel.DTO.transactions.get_transactions_response_dto import GetTransactionsResponseDTO, \
    ServiceGetTransactionResponseDTO, FineGetTransactionResponseDTO, ItemGetTransactionsResponseDTO, \
    GuestGetTransactionResponseDTO, RoomGetTransactionResponseDTO
from modules.hotel.db.transactions_repository import TransactionDatabaseRepository
from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_transaction_repo, get_room_price_repo


async def get_transactions(
    first_name: str | None = Query(None),
    last_name: str | None = Query(None),
    surname: str | None = Query(None),
    room_name: str | None = Query(None),
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
    room_price_repo: FineDatabaseRepository = Depends(get_room_price_repo),
):
    transactions = await transaction_repo.get_all_transactions(
        first_name=first_name,
        last_name=last_name,
        surname=surname,
        room_name=room_name,
    )

    # Преобразуем в DTO
    items = []
    for transaction in transactions:
        services = [ServiceGetTransactionResponseDTO.from_row(row) for row in
                    transaction.services_meta]
        fines = [FineGetTransactionResponseDTO.from_row(row) for row in transaction.fines_meta]

        room_price_obj = await room_price_repo.get(
            building=transaction.room_building, room_type=transaction.room_type
        )

        total_price = None
        if transaction.count_days:
            total_price = room_price_obj.price * transaction.count_days
        item = ItemGetTransactionsResponseDTO(
            id=transaction.id,
            guest=GuestGetTransactionResponseDTO.model_validate(transaction.guest),
            services=services,
            fines=fines,
            room=RoomGetTransactionResponseDTO(
                number=transaction.room_number,
                building=transaction.room_building,
                type=transaction.room_type,
                count_days=transaction.count_days,
                price=room_price_obj.price,
                total_price=total_price,
            ),
            payment_type=transaction.payment_type,
        )
        items.append(item)

    return GetTransactionsResponseDTO(transactions=items)
