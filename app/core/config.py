from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    BASE_URL_PREFIX: str = '/api/v1'
    PORT: int
    APP_RUNNING: str = f'app running on {os.getenv("PORT")}'
    SQLALCHEMY_DATABASE_URL = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_DATABASE")}'

    class Config:
        env_file = '.env'
        case_sensitive = True
        
settings = Settings()  # type: ignore 