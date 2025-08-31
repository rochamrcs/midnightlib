from sqlalchemy import text


def test_db_connection(session):
    result = session.execute(text("SELECT 1")).scalar()
    assert result == 1
