from fastapi import Depends

from modules.hotel.DTO.fines.get_fines_dto import GetFinesResponseDTO
from modules.hotel.db.fines_repository import FineDatabaseRepository
from modules.hotel.dependencies.get_obj_db import get_fine_repo


async def get_fines(
    fine_repo: FineDatabaseRepository = Depends(get_fine_repo),
):
    fines  = await fine_repo.get_all()
    fines_response = []
    for fine in fines:
        if not fine.is_deleted:
            fines_response.append(fine)
    return GetFinesResponseDTO(fines=fines_response)
