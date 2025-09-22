from pydantic import BaseModel


class BillAcceptorStatusResponseDTO(BaseModel):
    max_bill_count: int
    bill_count: int


class BillDispenserStatusResponseDTO(BaseModel):
    upper_box_value: int
    lower_box_value: int
    upper_box_count: int
    lower_box_count: int

class StatusSystemResponseDTO(BaseModel):
    bill_acceptor: BillAcceptorStatusResponseDTO | None
    bill_dispenser: BillDispenserStatusResponseDTO | None
    detail: str | None
