from fastapi import FastAPI
from bridges.app.router import api_router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=api_router)
    return app
