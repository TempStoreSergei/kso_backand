import json
from typing import Dict, Any, Optional

import httpx
from httpx_socks import AsyncProxyTransport

from api.configs.settings import settings
from api.configs.loggers import logger
from api.db_shop_api.errors import DBShopError


class BaseAPIClient:
    """Базовый HTTP клиент для работы с API 1С"""

    def __init__(self):
        self.base_url = settings.DATABASE_SHOP_URL
        self.auth = ('Кассир', '1234566')
        self.transport = AsyncProxyTransport.from_url("socks5://127.0.0.1:1080")

    async def _make_request(
            self,
            method: str,
            endpoint: str,
            data: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
    ):
        """Базовый метод для выполнения HTTP запросов"""
        url = f"{self.base_url}{endpoint}"

        max_retries = 3
        attempt = 0

        while attempt < max_retries:
            try:
                async with httpx.AsyncClient(auth=self.auth, timeout=30.0, transport=self.transport) as client:
                    if method.upper() == "GET":
                        response = await client.get(url, params=params)
                    elif method.upper() == "POST":
                        response = await client.post(url, json=data, params=params)
                    elif method.upper() == "PUT":
                        response = await client.put(url, json=data, params=params)
                    elif method.upper() == "DELETE":
                        response = await client.delete(url, params=params)
                    else:
                        raise ValueError(f"Неподдерживаемый HTTP метод: {method}")

                    response.raise_for_status()
                    try:
                        return response.json()
                    except (json.decoder.JSONDecodeError, ValueError):
                        return {}

            except httpx.HTTPStatusError as e:
                status = e.response.status_code
                error_data = self._handle_http_error(e)

                # Повторяем только если 5xx ошибка
                if 500 <= status < 600:
                    attempt += 1
                    logger.warning(f'HTTP {status} (попытка {attempt}) при запросе к {endpoint}')
                    if attempt >= max_retries:
                        raise DBShopError(
                            status_code=status,
                            message=f'Серверная ошибка 1С API (после {max_retries} попыток)',
                            response_data=error_data
                        )
                else:
                    # Ошибка 4xx — не повторяем
                    logger.error(f'Клиентская ошибка при запросе к 1С API {endpoint}: {error_data}')
                    raise DBShopError(
                        status_code=status,
                        message=f'Клиентская ошибка при запросе к 1С API {endpoint}',
                        response_data=error_data
                    )
            except httpx.RequestError as e:
                logger.error(f'Ошибка соединения с 1С API {endpoint}: {str(e)}')
                attempt += 1
                raise DBShopError(
                    status_code=503,
                    message=f'Ошибка соединения с 1С API',
                    response_data={"detail": str(e)}
                )

    @classmethod
    def _handle_http_error(cls, e: httpx.HTTPStatusError) -> Dict[str, Any]:
        """Обработка HTTP ошибок"""
        try:
            return e.response.json()
        except ValueError as json_error:
            logger.warning(f"Некорректный JSON в ответе от 1С API: {json_error}")
            return {
                "error": "invalid_json_response",
                "detail": getattr(e.response, 'text', '')[:500],
                "status_code": e.response.status_code
            }
        except Exception as unexpected_error:
            logger.error(f"Неожиданная ошибка при обработке ответа от 1С API: {unexpected_error}")
            return {
                "error": "unexpected_parsing_error",
                "detail": f"Ошибка обработки ответа: {str(unexpected_error)}"
            }
