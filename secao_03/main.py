from typing import Optional, Any, Dict, List
from fastapi import (
    FastAPI,
    HTTPException,
    Response,
    Path,
    Query,
    Header,
    Depends,
    status,
)
# from fastapi.responses import JSONResponse
from time import sleep

from models import Curso, cursos


def fake_db():
    try:
        print('Abrindo conexão com o Banco de Dados ...\n')
        sleep(1)
    finally:
        print('Fechando conexão com o Banco de Dados ...\n')
        sleep(1)


app = FastAPI(
    title='API de Cursos da Geek University',
    version='0.0.1',
    description='API para estudos de FastAPI Pytho n',
)


@app.get(
    '/cursos',
    description='Retorna todos os cursos disponíveis.',
    summary='Retorna todos os cursos',
    response_model=List[Curso],
    response_description='Cursos encontrados com sucesso'
)
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get(
    '/cursos/{curso_id}',
    description='Retorna um curso com o ID especificado ou um dicionário vazio.',
    summary='Retorna um curso',
    response_model=Curso
)
async def get_curso(curso_id: int = Path(title='ID do curso', description='O ID deve ser entre 1 e 2', gt=0, lt=3, ), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post(
    '/cursos',
    status_code=status.HTTP_201_CREATED,
    description='Cria um novo curso no Banco de Dados.',
    summary='Cria um curso',
    response_model=Curso
)
async def post_cursos(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    # del curso.id
    return curso


@app.put(
    '/cursos/{curso_id}',
    description='Atualiza o curso do ID especificado.',
    summary='Atualiza um curso',
    response_model=Curso
)
async def post_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Não existe curso com o ID')


@app.delete(
    '/cursos/{curso_id}',
    description='Deleta o curso do ID.',
    summary='Deleta um curso'
)
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
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
