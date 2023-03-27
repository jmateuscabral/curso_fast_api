from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.curso_model import CursoModel
from core.deps import get_session


# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # Type: ignore
Select.inherit_cache = True  # Type: ignore
# Fim Bypass


router = APIRouter()


# POST Cursos
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def post_curso(curso: CursoModel, db: AsyncSession = Depends((get_session))):
    novo_curso = CursoModel(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas,
    )
    db.add(novo_curso)
    await db.commit()
    return novo_curso


# GET Cursos
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CursoModel])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos


# GET Curso
@router.get('/{curso_id}', status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso: CursoModel = result.scalar_one_or_none()
        if curso:
            return curso
        else:
            raise HTTPException(detail='Curso não encontrado.', status_code=status.HTTP_404_NOT_FOUND)
        return cursos


# PUT Curso
@router.put('/{curso_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CursoModel)
async def put_curso(curso_id: int, curso: CursoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_update: CursoModel = result.scalar_one_or_none()
        if curso_update:
            curso_update.titulo = curso.titulo
            curso_update.aulas = curso.aulas
            curso_update.horas = curso.horas
            await session.commit()
            return curso_update
        else:
            raise HTTPException(detail='Curso não encontrado.', status_code=status.HTTP_404_NOT_FOUND)


# GET Curso
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del: CursoModel = result.scalar_one_or_none()
        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Curso não encontrado.', status_code=status.HTTP_404_NOT_FOUND)
        return cursos

