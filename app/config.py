from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

DB_FILE = BASE_DIR / "database.db"
DB_URI = f"sqlite:///{DB_FILE}"
DB_ECHO = False

SECRET_KEY = os.getenv("SECRET_KEY", "supersecrettoken123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = 30
