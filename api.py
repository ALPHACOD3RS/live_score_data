from fastapi import FastAPI
import scrap


app = FastAPI()


@app.get("/news")
async def root():
    return scrap.news()
