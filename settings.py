from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_DB: str = "tracker"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"

    REDIS_HOST: str = "cache"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: str|None = None
    JWT_SECRET_KEY:str = 'secret_key'
    JWT_ENCODE_ALGORITHM:str = 'HS256'
    
    @property
    def get_database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
