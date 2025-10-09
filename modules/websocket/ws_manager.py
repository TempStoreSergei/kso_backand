from fastapi import WebSocket
from pydantic import BaseModel

from modules.websocket.ws_dto import WSEventDTO, WSEventType, WSOrderDataDTO
from modules.websocket.loggers import logger


class WSManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active.remove(ws)

    async def broadcast(self, message: dict):
        for ws in self.active:
            await ws.send_json(message)
            logger.info(f'Отправлено внешнее сообщение в вебсокет: {message}')

    async def _send_to_all(self, message: BaseModel):
        """Внутренний метод для отправки сообщения всем подключенным клиентам."""
        message = message.model_dump()
        for ws in self.active:
            await ws.send_json(message)
            logger.info(f'Отправлено внутреннее сообщение в вебсокет: {message}')

    async def send_order(self, order_data: WSOrderDataDTO):
        message = WSEventDTO(
            event=WSEventType.get_order_data,
            data=order_data,
        )
        await self._send_to_all(message)

    async def send_error_payment(self):
        message = WSEventDTO(
            event=WSEventType.error_payment,
        )
        await self._send_to_all(message)


ws_manager = WSManager()
