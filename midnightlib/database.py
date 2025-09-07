from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from midnightlib.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def sanitization(data):
    sanitizaded = data.strip().lower()
    return sanitizaded
