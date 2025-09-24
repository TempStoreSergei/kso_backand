import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv("/home/fsadmin/kso/.env")


TERMINAL_ID = os.getenv("TERMINAL_ID", "d59b290c-69e5-465e-86d6-295f530f407")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
LOKI_URL = os.getenv("LOKI_URL", "http://192.168.0.247:3100/loki/api/v1/push")

BASE_DB_URL = os.getenv("BASE_DB_URL", "http://10.0.0.9/test_bigam_ut_maruta/hs/kassa")
BASE_DB_AUTH = (
    os.getenv("BASE_DB_USER", "rest"),
    os.getenv("BASE_DB_PASS", "tser"),
)
BASE_API_URL = os.getenv("BASE_API_URL", "http://localhost:8000")

MARK_API_URL = os.getenv("MARK_API_URL", "https://cdn.crpt.ru/api/v4/true-api/cdn/info")
MARK_API_KEY = os.getenv("MARK_API_KEY", "46996107-e4cf-4e72-a407-1f929dd7e0af")
FISCAL_DRIVE_NUMBER = os.getenv("FISCAL_DRIVE_NUMBER", "7380440801919544")


@dataclass(frozen=True)
class DBUrls:
    """Эндпоинты для запросов к API 1C."""
    BASKET: str = f"{BASE_DB_URL}/api/v1/carts/get_cart_by_qr_code"
    BARCODE: str = f"{BASE_DB_URL}/api/v1/items/get_item_by_baracode"
    FIRE_MARK: str = f"{BASE_DB_URL}/api/v1/items/get_item_by_fair_mark"
    CLIENT: str = f"{BASE_DB_URL}/api/v1/clients/get_client_by_qr_code"
    LOG: str = f"{BASE_DB_URL}/api/v1/logs"
    PROMO: str = f"{BASE_DB_URL}/api/v1/promo"


@dataclass(frozen=True)
class APIUrls:
    """Эндпоинты для запросов к внутреннему API."""
    BASKET: str = f"{BASE_API_URL}/api/v1/baskets/receive_fixed_basket"
    BARCODE: str = f"{BASE_API_URL}/api/v1/baskets/receive_dynamic_basket"
    CONS: str = f"{BASE_API_URL}/api/v1/consultants/receive_consultant"
    CLIENT: str = f"{BASE_API_URL}/api/v1/clients/receive_client"
    GIFT_CART: str = f"{BASE_API_URL}/api/v1/clients/receive_gift_cart"
    MESSAGE: str = f"{BASE_API_URL}/api/v1/baskets/broadcast_message"
