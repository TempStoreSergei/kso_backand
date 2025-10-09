from fastapi import Depends

from modules.screensaver.DTO.get_files_dto import GetFilesResponseDTO
from modules.screensaver.db.screensaver_repository import get_screensaver_file_repo, \
    ScreensaverFileDatabaseRepository


async def get_files(
    screensaver_file_repo: ScreensaverFileDatabaseRepository = Depends(get_screensaver_file_repo),
):
    files = await screensaver_file_repo.get_all()
    files_data = []
    for file in files:
        files_data.append({
            'id': file.id,
            'order': file.order,
            'fileUrl': file.file_url,
            'soundIsEnable': file.sound_is_enable,
            'timeShowImage': file.time_show_image,
            'fileType': file.file_type,
        })
    return GetFilesResponseDTO(files=files_data)
