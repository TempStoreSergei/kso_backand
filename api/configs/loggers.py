import logging
from logging.handlers import RotatingFileHandler

import colorlog


# Создание логгера
logger = logging.getLogger("Системный")
logger.setLevel(logging.DEBUG)

# Настраиваем форматтер
file_formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

# Формат сообщений
log_format = "[{asctime}] [{levelname:^8}] [{name}] {message}"
date_format = "%Y-%m-%d %H:%M:%S"

# Файл — без цвета
file_handler = RotatingFileHandler(
    "logs/api.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Консоль — с цветом всего сообщения
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

# Добавляем хендлеры
logger.addHandler(file_handler)
logger.addHandler(console_handler)
