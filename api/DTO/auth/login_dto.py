from pydantic import BaseModel


class LoginResponseDTO(BaseModel):
    detail: str
