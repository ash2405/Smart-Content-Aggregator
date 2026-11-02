from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    app_name: str =  "Smart Content Aggregator API"
    app_version: str = "0.1.0"
    debug: bool = False
    database_url: str
    news_api_url: str
    max_upload_size: int = 5 * 1024 * 1024  # 5 MB
    upload_dir: str = "uploads"

    model_config = SettingsConfigDict(
        env_file= ".env",
        env_file_encoding= "utf-8",
        case_sensitive= False
    )

def get_settings() -> Settings:
    return Settings()


settings = get_settings()