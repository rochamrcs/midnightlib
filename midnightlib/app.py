from http import HTTPStatus

from fastapi import FastAPI

from midnightlib.routers.users import user
from midnightlib.schemas import Message

app = FastAPI()

app.include_router(user.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message':
            'Bem-vindos(as) à MidnightLib System, onde sonhos e imaginação'
            'ganham forma através de palavras que farão você viajar '
            'pela mente dos melhores romancistas.'}
