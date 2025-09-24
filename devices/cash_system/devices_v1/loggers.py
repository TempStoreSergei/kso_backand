import logging
from logging.handlers import RotatingFileHandler


# Цвета ANSI для разных уровней
LEVEL_COLORS = {
    "DEBUG": "\033[94m",  # Синий
    "INFO": "\033[92m",  # Зелёный
    "WARNING": "\033[93m",  # Жёлтый
    "ERROR": "\033[91m",  # Красный
    "CRITICAL": "\033[95m",  # Пурпурный
}
RESET = "\033[0m"


class FullColorFormatter(logging.Formatter):
    """Класс форматирует сообщения логгера в разные цвета."""

    def format(self, record):
        """Функция форматирует сообщение логгера."""
        color = LEVEL_COLORS.get(record.levelname, "")
        # Обычное форматирование
        formatted = super().format(record)
        # Окрашиваем всю строку
        return f"{color}{formatted}{RESET}"


# Создание логгера
logger = logging.getLogger("Системный")
logger.setLevel(logging.DEBUG)
logger.propagate = False

# Формат сообщений
log_format = "[{asctime}] [{levelname:^8}] [{name}] {message}"
date_format = "%Y-%m-%d %H:%M:%S"

# Файл — без цвета
file_formatter = logging.Formatter(fmt=log_format, datefmt=date_format, style="{")
file_handler = RotatingFileHandler(
    "./api.log", maxBytes=5 * 1024 * 1024, backupCount=1, encoding="utf-8"
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Консоль — с цветом всего сообщения
console_formatter = FullColorFormatter(fmt=log_format, datefmt=date_format, style="{")
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

# Добавляем хендлеры
logger.addHandler(file_handler)
logger.addHandler(console_handler)
