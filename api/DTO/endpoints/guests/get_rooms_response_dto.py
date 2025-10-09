from pydantic import BaseModel, Field, ConfigDict


class ItemGetRoomsResponseDTO(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class GetRoomsResponseDTO(BaseModel):
    rooms: list[ItemGetRoomsResponseDTO]
