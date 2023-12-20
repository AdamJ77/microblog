from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.database.db import Database
from backend.api.logger import init_logger
from backend.api.routers import hello
from backend.api.routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_client = Database()
    app.database = await db_client.database
    yield
    await db_client.close()


def create_app():
    init_logger()
    # app = FastAPI(lifespan=lifespan)
    app = FastAPI()

    # including routers
    app.include_router(hello.router)
    app.include_router(auth.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


if __name__ == '__main__':
    create_app()
