from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import config

engine = create_engine(
    url=config.DB_URI,
    echo=config.DB_ECHO,
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def set_foreign_keys_on_for_sqlite(dbapi_con, connection_record):
    cursor = dbapi_con.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if config.DB_URI.startswith("sqlite://"):
    event.listen(
        engine,
        "connect",
        set_foreign_keys_on_for_sqlite,
    )
