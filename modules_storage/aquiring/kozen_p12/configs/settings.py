from pydantic_settings import BaseSettings


class AcquiringSettings(BaseSettings):
    ACQUIRING_CHANNEL: str
    class Config:
        env_file = "./modules/acquiring/.env"


acquiring_settings = AcquiringSettings()
