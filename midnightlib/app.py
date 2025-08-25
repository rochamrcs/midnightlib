from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Bem-vindos(as) à MidnightLib System, onde sonhos e imaginação '
    'ganham forma através de palavras que farão você viajar pela mente dos melhores romancistas.'}