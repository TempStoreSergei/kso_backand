from pydantic import BaseModel, Field


class AddFileRequestDTO(BaseModel):
    order: int = Field(examples=[1], description="Порядковый номер файла")
    file_base64: str = Field(
        examples=["data:image/jpeg;base64,/9j..."],
        description="Строка c файлом в формате base64",
        alias='fileBase64',
    )
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


class AddFileResponseDTO(BaseModel):
    file_id: int
    detail: str
