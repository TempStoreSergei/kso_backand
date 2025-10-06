from fastapi import WebSocket
from pydantic import BaseModel

from modules.websocket.ws_dto import WSEventDTO, WSEventType, WSOrderDataDTO


class WSManager:
    def __init__(self):
        self.active: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active.remove(ws)

    async def _send_to_all(self, message: BaseModel):
        """Внутренний метод для отправки сообщения всем подключенным клиентам."""
        message = message.model_dump()
        for ws in self.active:
            await ws.send_json(message)

    async def send_item(self, item_data: WSOrderDataDTO):
        message = WSEventDTO(
            event=WSEventType.get_one_item,
            data=item_data,
        )
        await self._send_to_all(message)


ws_manager = WSManager()
