import pytest
from app import app

@pytest.fixture(scope='session')
def flask_app():
    with app.test_client() as client:
        yield client

@pytest.fixture
def app():
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
