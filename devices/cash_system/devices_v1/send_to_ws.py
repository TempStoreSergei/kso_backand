import json
import websockets


async def send_to_ws(event: str, detail: str, data: dict | None = None):
    uri = "ws://localhost:8000/websockets/test_run_accepting_cash"
    try:
        async with websockets.connect(uri) as websocket:

            # Отправка тестового сообщения
            message = json.dumps({
                'event': event,
                'detail': detail,
                'data': data or {}
            })
            await websocket.send(message)

    except Exception as e:
        print(f"Ошибка: {e}")
