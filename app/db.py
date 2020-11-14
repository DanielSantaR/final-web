import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.config import Settings, get_settings

settings: Settings = get_settings()

log = logging.getLogger("uvicorn.info")  # new


def init_db(app: FastAPI) -> None:
    enviroment = settings.ENVIROMENT
    db_url = (
        settings.database_dev_url if enviroment == "dev" else settings.database_prod_url
    )
    log.info(f"connected to the database {db_url}")
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["app.infra.postgres.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
