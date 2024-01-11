from contextlib import asynccontextmanager
import os

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.api.database.db import Database
from backend.api.database import adapters
from backend.api.logger import init_logger
from backend.api.routers import hello, posts, auth, static_files
from backend.api.routers.static_files import STATIC_FOLDER_NAME


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_client = Database()
    app.database = await db_client.database
    app.post_storage = adapters.PostStorageDatabase(app.database)
    app.timeline = adapters.TimelineStorageDatabase(app.database)
    yield
    await db_client.close()


def create_app():
    router = APIRouter(
        prefix='/api',
        tags=['Auth']
    )
    # including routers
    router.include_router(hello.router)
    router.include_router(posts.router)
    router.include_router(auth.router)
    router.include_router(static_files.router)
    router.mount(
        "/static", StaticFiles(directory=STATIC_FOLDER_NAME), name="uploading")

    init_logger()
    app = FastAPI(lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    os.makedirs(STATIC_FOLDER_NAME, exist_ok=True)

    app.include_router(router)

    return app


if __name__ == "__main__":
    create_app()
