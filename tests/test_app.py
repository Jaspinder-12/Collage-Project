import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy before importing app to prevent ModuleNotFoundError or FileNotFoundError
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda template_name: b"home.html")
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict_invalid_input(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
