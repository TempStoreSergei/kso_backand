from fastapi import Depends, HTTPException, status

from modules.hotel.DTO.transactions.update_transaction_dto import UpdateTransactionRequestDTO, UpdateTransactionResponseDTO
from modules.hotel.db.transactions_repository import TransactionDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_transaction_repo


async def update_transaction(
    data: UpdateTransactionRequestDTO,
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
):
    guest = {
        'first_name': data.guest.first_name,
        'last_name': data.guest.last_name,
        'surname': data.guest.surname,
    }

    room = {
        'number': data.room.number,
        'type': data.room.type,
        'building': data.room.building,
    }

    transaction = await transaction_repo.update_transaction(
        transaction_id=data.id,
        guest=guest,
        room=room,
    )

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=''
        )

    return UpdateTransactionResponseDTO(
        transaction_id=transaction.id,
        detail=''
    )
