from fastapi.testclient import TestClient
from server import create_app
from server import models
import pytest

app = create_app()
client = TestClient(app)


@pytest.fixture()
def client():
    app = create_app()
    yield TestClient(app)


@pytest.fixture()
def max_index():
    return 36