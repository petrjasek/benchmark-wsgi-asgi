import random
import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    sleep_time = random.random()
    await asyncio.sleep(sleep_time)
    return {"message": "Hello world", "sleep": sleep_time}

