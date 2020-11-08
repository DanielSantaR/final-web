import os

import pytest
from starlette.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from app.config import Settings, get_settings
from app.main import create_application


def get_settings_override():
    return Settings(testing=1, database_dev_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="function")
def test_app():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as test_client:
        # testing
        yield test_client


@pytest.fixture(scope="module")
def test_app_with_db():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override

    # Link with DB for testing
    initializer(
        ["app.infra.postgres.models"], db_url=os.environ.get("DATABASE_TEST_URL"),
    )

    with TestClient(app) as test_client:
        # testing
        yield test_client

    # tear down
    finalizer()
