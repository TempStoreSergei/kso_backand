import asyncio

import websockets


async def listen():
    """Тестовый прослушиватель вебсокета."""
    uri = "ws://localhost:8005/ws"

    async with websockets.connect(uri) as websocket:
        print(f"Подключен к {uri}")

        async def receive_messages():
            while True:
                try:
                    message = await websocket.recv()
                    print(f"Получено сообщение: {message}")
                except websockets.ConnectionClosed:
                    print("Соединение закрыто")
                    break

        await receive_messages()


# Запускаем клиент
asyncio.run(listen())
