from fastapi import Depends, HTTPException, status

from modules.hotel.DTO.transactions.save_transaction_dto import AddTransactionResponseDTO, \
    AddTransactionRequestDTO
from modules.hotel.db.transactions_repository import GuestDatabaseRepository, TransactionDatabaseRepository
from modules.hotel.db.services_repository import ServiceDatabaseRepository
from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_guest_repo, get_transaction_repo, get_service_repo, get_fine_repo


async def save_transaction(
    transaction_data: AddTransactionRequestDTO,
    guest_repo: GuestDatabaseRepository = Depends(get_guest_repo),
    service_repo: ServiceDatabaseRepository = Depends(get_service_repo),
    fine_repo: FineDatabaseRepository = Depends(get_fine_repo),
    transaction_repo: TransactionDatabaseRepository = Depends(get_transaction_repo),
):
    guest = await guest_repo.get(**transaction_data.guest.model_dump())
    if not guest:
        guest = await guest_repo.create(**transaction_data.guest.model_dump())

    # Проверяем и собираем услуги
    services = []
    services_meta = []
    if transaction_data.services:
        for service_dto in transaction_data.services:
            service = await service_repo.get(id=service_dto.id)
            if not service:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'Услуга с id {service_dto.id} не найдена'
                )
            services.append(service)
            services_meta.append({
                'service': service,
                'count': service_dto.count or 1,
                'duration': service_dto.duration
            })

    # Проверяем и собираем штрафы
    fines = []
    fines_meta = []
    if transaction_data.fines:
        for fine_dto in transaction_data.fines:
            fine = await fine_repo.get(id=fine_dto.id)
            if not fine:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'Штраф с id {fine_dto.id} не найден'
                )
            fines.append(fine)
            fines_meta.append({
                'fine': fine,
                'count': fine_dto.count
            })

    # Создаём транзакцию через репозиторий
    new_transaction = await transaction_repo.create(
        guest_id=guest.id,
        room_number=transaction_data.room.number,
        room_type=transaction_data.room.type,
        room_building=transaction_data.room.building,
        count_days=transaction_data.room.count_days,
        payment_type=transaction_data.payment_type
    )

    # Добавляем услуги и штрафы через репозиторий
    await transaction_repo.add_services(new_transaction.id, services_meta)
    await transaction_repo.add_fines(new_transaction.id, fines_meta)

    return AddTransactionResponseDTO(
        transaction_id=new_transaction.id,
        detail='Транзакция успешно сохранена'
    )
