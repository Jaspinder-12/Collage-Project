import pytest
from unittest.mock import MagicMock
import sys

# Mock libraries to avoid ModuleNotFoundError or FileNotFoundError during test collection
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index_route(client, monkeypatch):
    # Mock render_template to test the route logic cleanly
    monkeypatch.setattr(
        app, "render_template", lambda template_name: b"Mocked Home Page"
    )
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mocked Home Page" in response.data


def test_predict_error_handling(client):
    # Missing required fields will trigger KeyError inside the route
    data = {"item_weight": "10.5"}
    response = client.post("/predict", data=data)

    # 🛡️ Sentinel: Expecting our secure 400 Bad Request error rather than an internal 500 crash
    assert response.status_code == 400
    assert b"Bad Request" in response.data
