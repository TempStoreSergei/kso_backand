from fastapi import Depends, Query

from api.DTO.endpoints.guests.get_transactions_response_dto import GetTransactionsResponseDTO
from api.db.guest_repository import TransactionDatabaseRepository
from api.dependencies.get_obj_db import get_transaction_repo


async def get_transactions(
    first_name: str | None = Query(None),
    last_name: str | None = Query(None),
    surname: str | None = Query(None),
    room_name: str | None = Query(None),
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
):
    transactions = await transaction_repo.get_all_transactions(
        first_name=first_name,
        last_name=last_name,
        surname=surname,
        room_name=room_name,
    )

    return GetTransactionsResponseDTO(transactions=transactions)
