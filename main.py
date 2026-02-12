from typing import Optional
from fastapi import FastAPI
import asyncio
from googletrans import Translator
import time
import random
from pydantic import BaseModel

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # or ["POST"] if you want to restrict
    allow_headers=["*"],
)


async def translate_text(text: str) -> str:
    async with Translator() as translator:
        try:
            result = await translator.translate(text, src='en', dest='hi')
        except Exception as e:
            print(f"Translation error: {e}")
            return ''
        return result.text 

class TranslateRequest(BaseModel):
    text: str


class TranslateResponse(BaseModel):
    original_text: str
    translated_text: str


app = FastAPI()


@app.post("/translate", response_model=TranslateResponse)
async def translate(req: TranslateRequest):
    translated = await translate_text(req.text)
    return TranslateResponse(
        original_text=req.text,
        translated_text=translated,
    )
    
if __name__ == "__main__":
    # Run the server when this file is executed directly
    uvicorn.run("translate_api:app", host="0.0.0.0", port=8000, reload=True)
