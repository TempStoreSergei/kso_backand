from pydantic_settings import BaseSettings


class CashSystemSettings(BaseSettings):
    PAYMENT_SYSTEM_CASH_CHANNEL: str
    class Config:
        env_file = "./modules/cash_system/.env"


cash_system_settings = CashSystemSettings()
