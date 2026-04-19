import sys
from unittest.mock import MagicMock

# Mock module-level joblib/numpy dependencies before app import
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402
import pytest  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"mock html")
    response = client.get("/")
    assert response.status_code == 200
