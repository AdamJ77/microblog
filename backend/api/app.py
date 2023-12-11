from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.database.db import Database
from backend.api.database import adapters
from backend.api.logger import init_logger
from backend.api.routers import hello, posts


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_client = Database()
    app.database = await db_client.database
    app.post_storage = adapters.PostStorageDatabaseAdapter(app.database)
    app.timeline = adapters.TimelineStorageDatabaseAdapter(app.database)
    yield
    await db_client.close()


def create_app():
    init_logger()
    app = FastAPI(lifespan=lifespan)

    # including routers
    app.include_router(hello.router)
    app.include_router(posts.router)

    return app


if __name__ == "__main__":
    create_app()
