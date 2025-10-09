from pydantic import BaseModel, Field, ConfigDict


class GetSettingsResponseDTO(BaseModel):
    is_enable: bool = Field(alias='isEnable', validation_alias='is_enable')
    sound_is_enable: bool = Field(alias='soundIsEnable', validation_alias='sound_is_enable')
    time_show_image: int = Field(alias='timeShowImage', validation_alias='time_show_image')
    idle_time: int = Field(alias='idleTime', validation_alias='idle_time')
    show_clock: bool = Field(alias='showClock', validation_alias='show_clock')

    model_config = ConfigDict(from_attributes=True)
