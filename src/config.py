import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
class Config:
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    MODEL_NAME = "llama3.2:3b-instruct-fp16"
    MAX_RETRIES = 3
    DOCUMENT_DIRECTORY = "../data"
