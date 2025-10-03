from pydantic import BaseModel, Field


class BillDispenserStatusResponseDTO(BaseModel):
    upper_box_value: int | None = Field(serialization_alias='upperBoxValue')
    lower_box_value: int | None = Field(serialization_alias='lowerBoxValue')
    upper_box_count: int | None = Field(serialization_alias='upperBoxCount')
    lower_box_count: int | None = Field(serialization_alias='lowerBoxCount')
    upper_cassette_size: int = Field(serialization_alias='upperCassetteSize')
    lower_cassette_size: int = Field(serialization_alias='lowerCassetteSize')
