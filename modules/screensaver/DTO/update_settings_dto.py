from pydantic import BaseModel, Field, ConfigDict


class UpdateSettingsRequestDTO(BaseModel):
    is_enable: bool | None = Field(
        None,
        examples=[True],
        description="Состояние скринсейвера (вкл/выкл)",
        alias='isEnable',
    )
    sound_is_enable: bool | None = Field(
        None,
        examples=[True],
        description="Состояние звука скринсейвера (вкл/выкл)",
        alias='soundIsEnable',
    )
    time_show_image: int | None = Field(
        None,
        examples=[200],
        description="Время показа изображения скринсейвера в секундах",
        alias='timeShowImage',
    )
    idle_time: int | None = Field(
        None,
        examples=[100],
        description="Время до активации скринсейвера в секундах",
        alias='idleTime',
    )
    show_clock: bool | None = Field(alias='showClock',)


class UpdateSettingsResponseDTO(BaseModel):
    detail: str
