from pydantic import BaseModel, Field, ConfigDict


class UpdateFileRequestDTO(BaseModel):
    id: int = Field(examples=[1], description="id файла")
    order: int = Field(examples=[1], description="Порядковый номер файла")
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


class UpdateFileResponseDTO(BaseModel):
    file_id: int
    detail: str
