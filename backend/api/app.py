from fastapi import FastAPI

from backend.api.logger import init_logger
from backend.api.routers import hello


def create_app():
    init_logger()
    app = FastAPI()

    # including routers
    app.include_router(hello.router)

    return app


if __name__ == '__main__':
    create_app()
