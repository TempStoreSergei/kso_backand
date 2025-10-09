from fastapi import Depends, HTTPException, status

from modules.screensaver.DTO.delete_file_dto import DeleteFileResponseDTO
from modules.screensaver.configs.files_storage import delete_file_from_minio
from modules.screensaver.db.screensaver_repository import get_screensaver_file_repo, \
    ScreensaverFileDatabaseRepository


async def delete_file(
    file_id: int,
    screensaver_file_repo: ScreensaverFileDatabaseRepository = Depends(get_screensaver_file_repo),
):
    file = await screensaver_file_repo.get(id=file_id)

    if not file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Файл заставки не найден"
        )

    if file.file_url:
        await delete_file_from_minio(file.file_url)

    await screensaver_file_repo.delete(id=file_id)

    return DeleteFileResponseDTO(
        detail='Файл заставки удален успешно',
    )
