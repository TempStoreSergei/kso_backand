from fastapi import Depends, HTTPException, status

from api.DTO.endpoints.guests.save_transaction_dto import AddTransactionResponseDTO, \
    AddTransactionRequestDTO
from api.db.guest_repository import GuestDatabaseRepository, TransactionDatabaseRepository, \
    ServiceDatabaseRepository
from api.dependencies.get_obj_db import get_guest_repo, get_transaction_repo, get_service_repo


async def save_transaction(
    transaction_data: AddTransactionRequestDTO,
    guest_repo: GuestDatabaseRepository = Depends(get_guest_repo),
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
):
    guest = await guest_repo.get(**transaction_data.guest.model_dump())
    if not guest:
        guest = await guest_repo.create(**transaction_data.guest.model_dump())

    services_data = transaction_data.services
    services=[]
    for service_id in services_data:
        service = await service_repo.get(id=service_id)
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Услуга не найдена'
            )
        services.append(service)

    new_transaction = await transaction_repo.create(
        guest=guest,
        services=services,
        room_id=transaction_data.room_id,
        check_in=transaction_data.check_in,
        check_out=transaction_data.check_out,
        payment_type=transaction_data.payment_type,
    )

    return AddTransactionResponseDTO(
        transaction_id=new_transaction.id,
        detail='Транзакция сохранена'
    )
