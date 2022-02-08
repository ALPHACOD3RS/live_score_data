from fastapi import FastAPI
import scrap


app = FastAPI()


@app.get("/api/news")
async def root():
    return scrap.news()
