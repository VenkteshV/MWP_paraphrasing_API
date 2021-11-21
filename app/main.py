from fastapi import FastAPI
from app.api.paraphraser import paraphraser

app = FastAPI()


@app.get('/health')
async def index():
    return {"health": "hello this is the paraphrasing API"}

app.include_router(paraphraser)