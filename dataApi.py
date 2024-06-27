from fastapi import FastAPI
from main import translate_text, trans_text

app = FastAPI()


@app.get('/uz_en/{text}')
async def uz_en(text: str):
    data = translate_text(text)
    return {
        "ENG": data
    }


@app.get('/en_uz/{text}')
async def en_uz(text: str):
    data = trans_text(text)
    return {
        "UZ": data
    }
