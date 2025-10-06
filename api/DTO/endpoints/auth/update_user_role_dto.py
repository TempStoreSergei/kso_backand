from typing import Annotated, Optional
from pydantic import BaseModel, Field, StringConstraints


class UpdateUserRoleRequestDTO(BaseModel):
    username: str
    role: Annotated[
        str,
        StringConstraints(strip_whitespace=True, to_lower=True, min_length=3, max_length=20)
    ] = Field(
        ...,
        example="admin",
        description="Новая роль пользователя"
    )


class UpdateUserRoleResponseDTO(BaseModel):
    id: int
    username: str
    role: Optional[str] = Field(None, description="Роль пользователя, если назначена")

    class Config:
        from_attributes = True
