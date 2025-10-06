from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class WSEventType(str, Enum):
    get_order_data = 'getOrderData'
    error_payment = 'errorPayment'
    success_payment = 'successPayment'


class WSEventDTO(BaseModel):
    event: WSEventType
    data: Any


class CartType(str, Enum):
    goods = 'goods' # товар
    services = 'services' # услуга


class CartItemDTO(BaseModel):
    id: str
    name: str
    quantity: int
    type: CartType
    price: int
    tax: int


class PaymentType(str, Enum):
    cash = 'cash'
    card = 'card'
    empty = '' # даем пользователю выбор


class WSOrderDataDTO(BaseModel):
    datetime: str
    sum: int
    avance: int
    type: str
    payment_type: PaymentType
    return_type: str
    cart: list[CartItemDTO]
    order: str
