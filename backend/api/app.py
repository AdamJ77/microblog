from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.database.db import Database
from backend.api.logger import init_logger
from backend.api.routers import hello
from backend.api.routers import login


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_client = Database()
    app.database = await db_client.database
    yield
    await db_client.close()


def create_app():
    init_logger()
    app = FastAPI()

    # including routers
    app.include_router(hello.router)
    app.include_router(login.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # You can replace "*" with specific origins if needed
        allow_credentials=True,
        allow_methods=["*"],  # You can replace "*" with specific HTTP methods
        allow_headers=["*"],  # You can replace "*" with specific headers
    )

    return app


if __name__ == '__main__':
    create_app()
