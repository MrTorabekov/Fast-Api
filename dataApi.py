from fastapi import FastAPI
from main import translate_text, trans_text

app = FastAPI()


@app.get('/uz_en/{name}')
async def uz_en(name: str):
    data = translate_text(name)
    return {
        "ENG": data
    }


@app.get('/en_uz/{namee}')
async def en_uz(namee: str):
    data = trans_text(namee)
    return {
        "UZ": data
    }
