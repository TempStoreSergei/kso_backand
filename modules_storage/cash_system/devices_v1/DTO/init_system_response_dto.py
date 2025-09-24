from pydantic import BaseModel


class InitSystemResponseDTO(BaseModel):
    status: bool
    detail: str | None
