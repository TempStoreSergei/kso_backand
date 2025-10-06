from redis.asyncio import Redis


from api.db_shop_api.base_client import BaseAPIClient
from api.configs.settings import settings
from api.db_shop_api.dto import PayOrderDTO

redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)


class DBShopClient(BaseAPIClient):
    """HTTP клиент для работы с API 1С."""
    async def get_order(self, code: str):
        """Получение клиента по qr коду."""
        return await self._make_request(
            "GET",
            "/check",
            params={"code": code},
        )

    async def pay_order(self, order_data: PayOrderDTO):
        """Получение консультанта по qr коду."""
        return await self._make_request(
            "POST",
            "/pay_order",
            data=order_data.model_dump(),
        )


db_shop_client = DBShopClient()
