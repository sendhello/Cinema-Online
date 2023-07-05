from contextlib import asynccontextmanager

from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from redis.asyncio import Redis

from api import router as api_router
from core.config import settings
from db import elastic, redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis.redis = Redis(host=settings.redis_host, port=settings.redis_port)
    elastic.es = AsyncElasticsearch(hosts=[f'http://{settings.elastic_host}:{settings.elastic_port}'])
    yield

    await redis.redis.close()
    await elastic.es.close()


app = FastAPI(
    lifespan=lifespan,
    title=settings.project_name,
    description="Информация о фильмах, жанрах и людях, участвовавших в создании произведения",
    version="1.0.0",
    docs_url='/api/api/openapi',
    openapi_url='/api/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(api_router, prefix='/api')
