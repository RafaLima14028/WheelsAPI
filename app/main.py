from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from loguru import logger

from schemas.generic import Message


logger.add(
    'logs/file_log.log',
    rotation="10 MB",
    retention="7 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    logger.info('FastAPI startup')
    yield
    logger.info('FastAPI shutdown')


app = FastAPI(
    title='WheelsAPI',
    version='0.0.1',
    lifespan=app_lifespan
)

# app.include_router()


@app.get("/", response_model=Message)
def home():
    return Message(message='Hello!!!')


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
