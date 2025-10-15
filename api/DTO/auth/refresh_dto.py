from pydantic import BaseModel


class RefreshResponseDTO(BaseModel):
    detail: str
