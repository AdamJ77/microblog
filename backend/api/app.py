from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.database.db import Database
from backend.api.logger import init_logger
from backend.api.routers import hello


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_client = Database()
    app.database = await db_client.database
    yield
    await db_client.close()


def create_app():
    init_logger()
    app = FastAPI(lifespan=lifespan)

    # including routers
    app.include_router(hello.router)

    return app


if __name__ == '__main__':
    create_app()
