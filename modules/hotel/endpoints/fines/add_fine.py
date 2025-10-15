from fastapi import Depends

from modules.hotel.DTO.fines.add_fine_dto import AddFineRequestDTO, AddFineResponseDTO
from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_fine_repo


async def add_fine(
    fine_data: AddFineRequestDTO,
    fine_repo: FineDatabaseRepository = Depends(get_fine_repo),
):
    fine  = await fine_repo.create(
        name=fine_data.name,
        price=fine_data.price,
        type=fine_data.type,
    )
    return AddFineResponseDTO(id=fine.id, detail='Штраф добавлена успешно')
