# Настройки фискального модуля

Этот модуль содержит настройки для работы с фискальными устройствами.

## Структура

- `settings.py` - класс настроек `FiscalSettings` с параметрами по умолчанию
- Настройки загружаются из `.env` файла в корне проекта

## Параметры настроек

### Кассир по умолчанию

```env
CASHIER_NAME="Кассир Иванов И."
CASHIER_INN="123456789047"
```

Используется как значение по умолчанию для всех фискальных операций, если кассир не установлен динамически через API `/cashier/set`.

### Компания

```env
COMPANY_INN="7701234567"
COMPANY_PAYMENT_ADDRESS="г. Москва, ул. Ленина, д. 1"
COMPANY_EMAIL="company@example.com"
```

### ATOL Драйвер (для queue worker)

```env
# Тип подключения: tcp, usb, serial, bluetooth
ATOL_CONNECTION_TYPE=tcp
ATOL_HOST=192.168.1.100
ATOL_PORT=5555

# Для serial подключения:
ATOL_SERIAL_PORT=/dev/ttyS0
ATOL_BAUDRATE=115200

# Путь к библиотеке libfptr10 (если не в системных путях)
ATOL_DRIVER_PATH=/usr/local/lib/libfptr10.so
```

### Redis

```env
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Пути

```env
LOG_DIR=logs
RECEIPTS_DIR=data/receipts
```

## Использование в коде

```python
from modules.fiscal.configs.settings import fiscal_settings

# Получить имя кассира по умолчанию
cashier_name = fiscal_settings.cashier_name

# Получить настройки Redis
redis_host = fiscal_settings.redis_host
redis_port = fiscal_settings.redis_port
```

## Приоритет настроек кассира

1. **Параметры запроса** - переданные в конкретном API запросе
2. **Динамические (Redis)** - установленные через `/cashier/set`
3. **Настройки (.env)** - значение `CASHIER_NAME` и `CASHIER_INN`

## Связь с queue worker

Queue worker (`/queue/settings.py`) использует те же переменные окружения из `.env` файла, поэтому настройки синхронизированы между FastAPI backend и queue worker.
