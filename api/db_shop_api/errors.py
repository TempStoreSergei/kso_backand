from typing import Optional, Dict


class DBShopError(Exception):
    """Исключение для ошибок 1С API"""
    def __init__(self, status_code: int, message: str, response_data: Optional[Dict] = None):
        self.status_code = status_code
        self.message = f'{response_data.get("detail")}'
        super().__init__(f"1C API Error. {status_code}: {message}")
