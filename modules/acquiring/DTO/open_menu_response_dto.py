from pydantic import BaseModel


class OpenMenuResponseDTO(BaseModel):
    status: bool
    detail: str | None
