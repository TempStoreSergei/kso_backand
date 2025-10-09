from fastapi import Depends

from api.DTO.endpoints.guests.update_transaction_dto import UpdateTransactionRequestDTO, UpdateTransactionResponseDTO
from api.db.guest_repository import GuestDatabaseRepository, TransactionDatabaseRepository, \
    ServiceDatabaseRepository
from api.dependencies.get_obj_db import get_guest_repo, get_transaction_repo, get_service_repo


async def update_transaction(
    data: UpdateTransactionRequestDTO,
    guest_repo: GuestDatabaseRepository = Depends(get_guest_repo),
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
):
    pass
