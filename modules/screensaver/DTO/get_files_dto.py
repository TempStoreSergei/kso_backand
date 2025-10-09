from pydantic import BaseModel, Field, ConfigDict


class ItemGetFilesResponseDTO(BaseModel):
    id: int
    order: int = Field(examples=[1], description="Порядковый номер файла")
    file_url: str = Field(alias='fileUrl')
    sound_is_enable: bool = Field(
        examples=[True],
        description="Состояние звука на видеофайле (вкл/выкл)",
        alias='soundIsEnable',
    )
    time_show_image: int = Field(
        examples=[200],
        description="Время показа изображения",
        alias='timeShowImage',
    )
    file_type: str = Field(alias='fileType')

    model_config = ConfigDict(from_attributes=True)


class GetFilesResponseDTO(BaseModel):
    files: list[ItemGetFilesResponseDTO]
