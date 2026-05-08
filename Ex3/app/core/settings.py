import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Banking AI-Agent"
    
    # Ollama Configuration
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "gpt-oss:20b")
    
    # Intent Model Configuration (from Lab 2)
    INTENT_MODEL_PATH: str = os.getenv("INTENT_MODEL_PATH", "../../Ex2/models/intent_model/")
    INTENT_CONFIG_PATH: str = os.getenv("INTENT_CONFIG_PATH", "app/core/inference.yaml")
    
    # Workflow Settings
    VALIDATION_ENABLED: bool = True
    MAX_TOKENS: int = 512

settings = Settings()
