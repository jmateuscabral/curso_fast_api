from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter ao menos três palavras.')
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')
        return value

    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 12:
            raise ValueError('O curso deve possuir mais de 12 aulas.')
        return value

    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 8:
            raise ValueError(f'O curso deve possuir mais de oito horas.')
        return value


cursos = [
    Curso(id=1, titulo='Curso de Programação Python', aulas=146, horas=65),
    Curso(id=2, titulo='Curso de API com FastAPI', aulas=47, horas=13),
    Curso(id=3, titulo='Curso de Programação Paralela com Python', aulas=23, horas=9),
    Curso(id=4, titulo='Curso de React', aulas=188, horas=67),
    Curso(id=5, titulo='Algorítmos e Lógica de Programação', aulas=28, horas=15),
]
