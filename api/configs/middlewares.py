import uuid
from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import Request, Response

from api.configs.loggers import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_body_length: int = 1000):
        super().__init__(app)
        self.max_body_length = max_body_length

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_id = str(uuid.uuid4())[:8]

        # --- Получаем параметры запроса ---
        query_params = dict(request.query_params)

        # --- Логируем запрос ---
        body_bytes = await request.body()
        try:
            body_text = body_bytes.decode()
        except Exception:
            body_text = str(body_bytes)
        logger.info(
            f"[{request_id}] --> {request.method} {request.url.path}\n"
            f"  Query Params: {query_params if query_params else 'None'}\n"
            f"  Body: {self._truncate(body_text)}"
        )

        # --- Обрабатываем запрос ---
        response = await call_next(request)

        # --- Перехватываем тело ответа ---
        response_body = b"".join([chunk async for chunk in response.body_iterator])

        # --- Логируем тело ---
        try:
            body_str = response_body.decode()
        except Exception:
            body_str = str(response_body)
        logger.info(f"[{request_id}] <-- {request.method} {request.url.path}\n"
                    f"Status: {response.status_code}\n"
                    f"Body: {self._truncate(body_str)}")

        # --- Восстанавливаем тело для клиента ---
        response.body_iterator = self._create_iterator(response_body)
        return response

    async def _create_iterator(self, body: bytes):
        yield body

    def _truncate(self, text: str) -> str:
        if len(text) > self.max_body_length:
            return text[:self.max_body_length] + f"... (truncated, total {len(text)} chars)"
        return text
