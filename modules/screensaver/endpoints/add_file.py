from fastapi import Depends, HTTPException, status

from modules.screensaver.DTO.add_file_dto import AddFileRequestDTO, AddFileResponseDTO
from modules.screensaver.configs.files_storage import upload_file_in_minio
from modules.screensaver.db.screensaver_repository import get_screensaver_file_repo, \
    ScreensaverFileDatabaseRepository


async def add_file(
    file_data: AddFileRequestDTO,
    screensaver_file_repo: ScreensaverFileDatabaseRepository = Depends(get_screensaver_file_repo),
):
    try:
        file_url, file_type = await upload_file_in_minio(
            file_data.file_base64, "screensaver-files"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Ошибка при загрузке медиа файла: {e}"
        )

    file = await screensaver_file_repo.create(
        order=file_data.order,
        file_url=file_url,
        sound_is_enable=file_data.sound_is_enable,
        time_show_image=file_data.time_show_image,
        file_type=file_type,
    )

    return AddFileResponseDTO(
        file_id=file.id,
        detail='Файл заставки добавлен успешно',
    )
