from pydantic import BaseModel


class ChangePasswordRequestDTO(BaseModel):
    old_password: str
    new_password: str


class ChangePasswordResponseDTO(BaseModel):
    detail: str
