import sys
from unittest.mock import MagicMock
import pytest

# Mock libraries to avoid ModuleNotFoundError and FileNotFoundError during collection
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client(monkeypatch):
    app.app.config["TESTING"] = True
    # Mock render_template to avoid needing HTML files during basic route testing
    monkeypatch.setattr(app, "render_template", lambda template_name, **kwargs: b"Mocked Render")
    with app.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mocked Render" in response.data
