import sys
from unittest.mock import MagicMock
import pytest

sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app as app_module  # noqa: E402


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"BigMart Sales Prediction" in response.data
