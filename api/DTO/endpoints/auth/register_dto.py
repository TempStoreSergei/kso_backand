from typing import Optional, Annotated
from pydantic import BaseModel, Field, StringConstraints


class RegisterRequestDTO(BaseModel):
    name: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=3, max_length=50)
    ] = Field(..., example="johndoe")

    password: Annotated[
        str,
        StringConstraints(min_length=6, max_length=128)
    ] = Field(..., example="securepassword123")


class RegisterResponseDTO(BaseModel):
    id: int
    username: str
    role: str
