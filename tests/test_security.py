import os

from dotenv import load_dotenv
from jwt import decode

from midnightlib.security import create_access_token

load_dotenv()


def test_jwt():
    data = {'test': 'test'}
    token = create_access_token(data)

    decoded = decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])

    assert decoded['test'] == data['test']
    assert 'exp' in decoded
