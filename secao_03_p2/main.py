from fastapi import FastAPI
from routes import curso_router, usuario_router

app = FastAPI()
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
