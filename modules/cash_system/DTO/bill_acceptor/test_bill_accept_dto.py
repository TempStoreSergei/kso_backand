from enum import Enum

from pydantic import BaseModel


class AmountValue(int, Enum):
    amount_10 = 1000
    amount_50 = 5000
    amount_100 = 10000
    amount_200 = 20000
    amount_500 = 50000
    amount_1000 = 100000
    amount_2000 = 200000
    amount_5000 = 500000


class TestBillAcceptRequestDTO(BaseModel):
    amount: AmountValue


class TestBillAcceptResponseDTO(BaseModel):
    status: bool
    detail: str
