from dotenv import load_dotenv
import os

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_PORT = os.getenv("QDRANT_PORT")
OPENAI_API_KEY = os.getenv("OPENAI_KEY")
