from pydantic import BaseModel


class ChangeUserPasswordRequestDTO(BaseModel):
    old_password: str
    new_password: str


class ChangeUserPasswordResponseDTO(BaseModel):
    detail: str
