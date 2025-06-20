from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    broker_url:str
    broker_port:str
    broker_username:str
    broker_password:str
    supabase_url:str
    supabase_api_key:str
    class Config:
        env_file=".env"
settings=Settings()