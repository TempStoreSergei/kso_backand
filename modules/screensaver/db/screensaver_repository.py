from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.base_database_repository import BaseDatabaseRepository
from api.configs.database import get_async_session
from modules.screensaver.models.models import ScreensaverFile, ScreensaverSettings


class ScreensaverFileDatabaseRepository(BaseDatabaseRepository):
    model_class = ScreensaverFile


class ScreensaverSettingsDatabaseRepository(BaseDatabaseRepository):
    model_class = ScreensaverSettings


async def get_screensaver_file_repo(session: AsyncSession = Depends(get_async_session)):
    yield ScreensaverFileDatabaseRepository(session)


async def get_screensaver_settings_repo(session: AsyncSession = Depends(get_async_session)):
    yield ScreensaverSettingsDatabaseRepository(session)
