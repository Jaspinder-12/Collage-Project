import pytest
import sys
from unittest.mock import MagicMock

# Mock external dependencies to avoid FileNotFoundError locally
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()
import app # noqa: E402

@pytest.fixture
def client(monkeypatch):
    app.app.config['TESTING'] = True
    # Mock render_template to avoid missing templates during tests
    monkeypatch.setattr(app, 'render_template', lambda *args, **kwargs: b"Mock Template Rendered")
    with app.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predict_invalid_input(client):
    response = client.post("/predict", data={"item_weight": "invalid"})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
