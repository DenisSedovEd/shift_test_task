from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

DB_FILE = BASE_DIR / "database.db"
DB_URI = f"sqlite:///{DB_FILE}"
DB_ECHO = False
