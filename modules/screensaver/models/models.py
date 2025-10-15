from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from api.configs.database import Base


class ScreensaverSettings(Base):
    """
    Модель настроек скринсейвера.

    Attrs:
        id (int): Уникальный идентификатор настроек.
        is_enable (bool): Включён ли скринсейвер.
        sound_enable (bool): Включен ли звук во время показа.
        time_show_image (int): Время показа одного изображения (в миллисекундах).
        idle_time (int): Время простоя до запуска скринсейвера (в миллисекундах).
        show_clock (bool): Показывать ли часы на экране скринсейвера.
    """
    __tablename__ = "screensaver_settings"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_enable: Mapped[bool] = mapped_column(Boolean)
    sound_is_enable: Mapped[bool] = mapped_column(Boolean)
    time_show_image: Mapped[int] = mapped_column(Integer)
    idle_time: Mapped[int] = mapped_column(Integer)
    show_clock: Mapped[bool] = mapped_column(Boolean)


class ScreensaverFile(Base):
    """
    Модель файлов скринсейвера.

    Attrs:
        id (int): Уникальный идентификатор файла.
        order (int): Порядок отображения файла в последовательности.
        file_url (str): URL или путь к файлу (изображение или видео).
        sound_is_enable (bool | None): Включен ли звук при воспроизведении данного файла.
        time_show_image (int | None): Время показа изображения (в миллисекундах);
        если None, используется значение по умолчанию.
        file_type (str): Тип файла (например, 'image' или 'video').
    """
    __tablename__ = "screensaver_files"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order: Mapped[int] = mapped_column(Integer)
    file_url: Mapped[str] = mapped_column(String)
    sound_is_enable: Mapped[bool] = mapped_column(Boolean, nullable=True)
    time_show_image: Mapped[int] = mapped_column(Integer, nullable=True)
    file_type: Mapped[str] = mapped_column(String)
