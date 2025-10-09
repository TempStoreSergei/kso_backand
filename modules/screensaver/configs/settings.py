from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    MINIO_URL: str
    class Config:
        env_file = "./modules/screensaver/.env"


settings = Settings()
