import logging
from logging.handlers import RotatingFileHandler

import colorlog


def get_logger(name: str, log_file: str = "logs/api.log") -> logging.Logger:
    """
    Создаёт и возвращает настроенный логгер с консолью и файловым логированием.

    :param name: имя логгера
    :param log_file: путь до файла логов
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Форматтер для файла
    file_formatter = logging.Formatter(
        fmt="%(name)s | %(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Форматтер для консоли с цветом
    console_formatter = colorlog.ColoredFormatter(
        "%(name)s | %(log_color)s%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    # Файл
    file_handler = RotatingFileHandler(
        log_file, maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    # Консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)

    # Чтобы не дублировались хендлеры при повторном вызове
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = get_logger("Системный")
