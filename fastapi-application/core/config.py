from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pydantic import PostgresDsn


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class ApiPrefix(BaseModel):
    prefix: str = "/api"

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=("/Users/admin/itshka/FastAPI_beta/fastapi-application/.env.template","/Users/admin/itshka/FastAPI_beta/fastapi-application/.env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP__CONFIG__",
    )
    db: DatabaseConfig
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()