from fastapi import FastAPI


app = FastAPI()


@app.get('/mensagem')
async def mensagem():
    return {
        'msg': 'Hello World!!'
    }

# O módulo fcntl não está disponível para Windows
# Deve ser instalado o micropython-fcntl

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
