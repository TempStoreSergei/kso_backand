from pydantic import BaseModel, Field


class BillAcceptorStatusResponseDTO(BaseModel):
    cassette_size: int = Field(serialization_alias='cassetteSize')
    max_bill_count: int | None = Field(serialization_alias='maxBillCount')
    bill_count: int | None = Field(serialization_alias='billCount')
