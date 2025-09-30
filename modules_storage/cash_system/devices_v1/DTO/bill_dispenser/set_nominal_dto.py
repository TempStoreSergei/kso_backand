from pydantic import BaseModel, Field


class SetNominalRequestDTO(BaseModel):
    upper_lvl: int = Field(alias='upperLvl')
    lower_lvl: int = Field(alias='lowerLvl')


class SetNominalResponseDTO(BaseModel):
    status: bool
    detail: str
