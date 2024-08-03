import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ABLY_API_KEY: str = os.getenv("ABLY_API_KEY")

settings = Settings()