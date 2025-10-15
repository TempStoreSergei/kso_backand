from pydantic import BaseModel


class GetRoomsResponseDTO(BaseModel):
    rooms1: list[str]
    rooms2: list[str]
    rooms3: list[str]
