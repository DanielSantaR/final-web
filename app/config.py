import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    database_dev_url: AnyUrl = os.environ.get("DATABASE_DEV_URL")
    database_prod_url: AnyUrl = os.environ.get("DATABASE_PROD_URL")
    testing: bool = os.getenv("TESTING", 0)
    ENVIROMENT: str = os.getenv("ENVIROMENT")
    WEB_APP_TITLE: str = os.getenv("WEB_APP_TITLE")
    WEB_APP_DESCRIPTION: str = os.getenv("WEB_APP_DESCRIPTION")
    WEB_APP_VERSION: str = os.getenv("WEB_APP_VERSION")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
