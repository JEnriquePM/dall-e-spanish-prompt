from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'dall-e-spanish-prompt'
    api_key: str
    org_id: str

    class Config:
        env_file = ".env"
