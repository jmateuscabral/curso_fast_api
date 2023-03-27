from typing import Optional
from fastapi import (
    FastAPI,
    HTTPException,
    Response,
    Path,
    Query,
    Header,
    status,
)
# from fastapi.responses import JSONResponse

from models import Curso

app = FastAPI()


cursos = {
    1: {
        'titulo': 'Programação com Python',
        'aulas': 120,
        'horas': 62,
    },
    2: {
        'titulo': 'Python Assíncrono',
        'aulas': 34,
        'horas': 11,
    },
    3: {
        'titulo': 'FastAPI',
        'aulas': 86,
        'horas': 27,
    },
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso', description='O ID deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_cursos(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put('/cursos/{curso_id}')
async def post_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não existe curso com o ID')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        curso = cursos[curso_id]
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não existe curso com o ID')


@app.get('/calculadora')
async def calculadora(a: int = Query(gt=5), b: int = Query(gt=15), x_geek: str = Header(default=None), c: Optional[int] = None):
    resultado = a + b
    if c:
        resultado += c
    print(f'X_GEEK: {x_geek}')
    return {'resultado': resultado}
