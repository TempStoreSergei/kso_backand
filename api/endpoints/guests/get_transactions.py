from fastapi import Depends

from api.DTO.endpoints.guests.get_transactions_response_dto import GetTransactionsResponseDTO
from api.db.guest_repository import TransactionDatabaseRepository
from api.dependencies.get_obj_db import get_transaction_repo


async def get_transactions(
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
):
    transactions = await transaction_repo.get_all_transactions()
    return GetTransactionsResponseDTO(transactions=transactions)
