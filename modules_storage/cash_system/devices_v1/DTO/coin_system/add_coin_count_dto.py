from pydantic import BaseModel, Field, model_validator


class AddCoinCountRequestDTO(BaseModel):
    coin_100: int | None = Field(alias='100')
    coin_200: int | None = Field(alias='200')
    coin_500: int | None = Field(alias='500')
    coin_1000: int | None = Field(alias='1000')

    @model_validator(mode='before')
    def at_least_one_coin(cls, values):
        if not any(values.get(field) is not None for field in
                   ['coin_100', 'coin_200', 'coin_500', 'coin_1000']):
            raise ValueError("Должно быть передано хотя бы одно значение монеты")
        return values


class AddCoinCountResponseDTO(BaseModel):
    coin_100: int = Field(serialization_alias='100')
    coin_200: int = Field(serialization_alias='200')
    coin_500: int = Field(serialization_alias='500')
    coin_1000: int = Field(serialization_alias='1000')
