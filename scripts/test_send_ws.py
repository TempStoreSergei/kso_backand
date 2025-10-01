import asyncio
import websockets
import json


async def send_to_ws(event: str, data: dict | None = None):
    message = {"event": event, "data": data}
    async with websockets.connect("ws://localhost:8000/ws") as ws:
        await ws.send(json.dumps(message))
        print(f"Отправлено: {message}")


if __name__ == "__main__":
    asyncio.run(send_to_ws("test_event", {"name": "test_product"}))
