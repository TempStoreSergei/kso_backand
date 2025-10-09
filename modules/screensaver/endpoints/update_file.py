from fastapi import Depends, HTTPException, status

from modules.screensaver.DTO.upadte_file_dto import UpdateFileRequestDTO, UpdateFileResponseDTO
from modules.screensaver.configs.files_storage import delete_file_from_minio, upload_file_in_minio
from modules.screensaver.db.screensaver_repository import get_screensaver_file_repo, \
    ScreensaverFileDatabaseRepository


async def update_file(
    file_data: UpdateFileRequestDTO,
    screensaver_file_repo: ScreensaverFileDatabaseRepository = Depends(get_screensaver_file_repo),
):
    file = await screensaver_file_repo.get(id=file_data.id)

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Файл заставки не найден'
        )

    updated_data = {}

    if file_data.order is not None:
        updated_data['order'] = file_data.order
    if file_data.sound_is_enable is not None:
        updated_data['sound_is_enable'] = file_data.sound_is_enable
    if file_data.time_show_image is not None:
        updated_data['time_show_image'] = file_data.time_show_image

    updated_file = await screensaver_file_repo.update(
        filters={'id': file_data.id},
        values=updated_data
    )

    return UpdateFileResponseDTO(
        file_id=updated_file.id,
        detail='Файл заставки изменен успешно',
    )
