from pydantic import BaseModel


class CheckConnectResponseDTO(BaseModel):
    status: bool
    detail: str | None
