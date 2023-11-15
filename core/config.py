from pydantic import BaseModel, AnyUrl

class Settings(BaseModel):
    app_name: str = "My FastAPI App"
    app_version: str = "1.0.0"
    app_port: int = 8000

    database_url: str = "sqlite:///./app.db"
    # Add other configuration parameters as needed

    class Config:
        env_file = ".env"
        case_sensitive = True

# Instantiate the Settings model to access the configuration
settings = Settings()
