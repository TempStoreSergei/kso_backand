import logging
from logging.handlers import RotatingFileHandler

from send_log_loki import send_loki

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler("scanner.log", maxBytes=5 * 1024 * 1024, backupCount=2),
        logging.StreamHandler(),
    ],
)
# Заглушаем httpx и httpcore
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.CRITICAL + 1)

logger = logging.getLogger(__name__)

class LokiHandler(logging.Handler):
    def emit(self, record):
        try:
            message = self.format(record)
            level = record.levelname.upper()
            send_loki(level, message)
        except Exception:
            self.handleError(record)

# Создаём хендлер для Loki
loki_handler = LokiHandler()
loki_handler.setLevel(logging.DEBUG)  # или нужный уровень
loki_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Добавляем к логгеру
logger.addHandler(loki_handler)
