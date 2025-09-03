from sqlalchemy import Select


def test_db_connection(session):
    result = session.execute(Select(1)).scalar()
    assert result == 1
