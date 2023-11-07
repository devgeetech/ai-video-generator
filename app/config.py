from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    open_ai_api_key: str
    murf_ai_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
