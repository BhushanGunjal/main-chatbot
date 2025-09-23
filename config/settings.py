from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    chroma_db_path: str = os.getenv("CHROMA_DB_PATH")
    env: str = os.getenv("ENV")

settings = Settings()
