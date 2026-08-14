from fastapi import FastAPI

from api.routes import router
from database.models import initialize


def create_app() -> FastAPI:
    app = FastAPI(title="CyberLab API", version="0.1.0")

    @app.on_event("startup")
    def startup() -> None:
        initialize()

    app.include_router(router, prefix="/api")
    return app
