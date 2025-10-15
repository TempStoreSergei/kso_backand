from fastapi import Depends

from modules.hotel.DTO.fines.update_fine_dto import UpdateFineRequestDTO, UpdateFineResponseDTO
from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_fine_repo


async def update_fine(
    updated_data: UpdateFineRequestDTO,
    fine_repo: FineDatabaseRepository = Depends(get_fine_repo),
):
    update_fields = {k: v for k, v in updated_data.dict(exclude_unset=True).items() if k != "id"}

    fine = await fine_repo.update(
        filters={'id': updated_data.id},
        values=update_fields
    )
    return UpdateFineResponseDTO(
        id=fine.id,
        detail='Штраф изменен успешно',
    )
