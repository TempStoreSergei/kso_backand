from pydantic_settings import BaseSettings


class CashSystemSettings(BaseSettings):
    PAYMENT_SYSTEM_CASH_CHANNEL: str
    CASSETTE_SIZE: int
    UPPER_CASSETTE_SIZE: int
    LOWER_CASSETTE_SIZE: int
    class Config:
        env_file = "./modules/cash_system/.env"


cash_system_settings = CashSystemSettings()
