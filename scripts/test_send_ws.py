import asyncio
import websockets
import json


async def send_to_ws(event: str, data: dict | None = None):
    message = {"event": event, "data": data}
    async with websockets.connect("ws://localhost:8005/ws") as ws:
        await ws.send(json.dumps(message))
        print(f"Отправлено: {message}")


if __name__ == "__main__":
    asyncio.run(send_to_ws("successPayment", {'rrn': '1234567891234'}))
    # asyncio.run(send_to_ws("errorPayment", {'rrn': '1234567891234'}))
    # asyncio.run(send_to_ws("getOrderData", {
    #     "datetime": "2025-09-16 11:37:40",
    #     "sum": 2800,
    #     "avance": 0,
    #     "type": "order",
    #     "payment_type": "",
    #     "return_type": "",
    #     "cart": [
    #         {
    #             "id": "622d0497-258c-11e1-1599-0030485d4164",
    #             "name": "ОБРАБОТКА ПО ПЛОСКОСТИ БЦ (фрезеровка)",
    #             "quantity": 1,
    #             "type": "services",
    #             "price": 2800,
    #             "tax": -1
    #         }
    #     ],
    #     "order": "673a97e0-92d8-11f0-8dab-000c29b2658c"
    # }))
