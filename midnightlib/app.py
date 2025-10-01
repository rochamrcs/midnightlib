import asyncio
import sys
from http import HTTPStatus

from fastapi import FastAPI

from midnightlib.routers.auth import auth
from midnightlib.routers.users import user
from midnightlib.schemas import Message

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message':
            'Bem-vindos(as) à MidnightLib System, onde sonhos e imaginação'
            'ganham forma através de palavras que farão você viajar '
            'pela mente dos melhores romancistas.'}
