from pydantic import BaseModel, Field


class AddRoomRequestDTO(BaseModel):
    name: str


class AddRoomResponseDTO(BaseModel):
    id: int
    detail: str
