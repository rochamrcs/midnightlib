import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from midnightlib.app import app

load_dotenv()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)

    with Session(engine) as session:
        yield session
