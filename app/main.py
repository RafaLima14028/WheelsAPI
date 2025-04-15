from fastapi import FastAPI
from contextlib import asynccontextmanager

from loguru import logger

from app.schemas.generic import Message

from app.api.auth import router as router_auth
from app.api.users import router as router_users
from app.api.vehicles import router as router_vehicles
from app.api.sales import router as router_sales

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

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_vehicles)
app.include_router(router_sales)


@app.get("/", response_model=Message)
def home():
    return Message(message='Hello, World!')
