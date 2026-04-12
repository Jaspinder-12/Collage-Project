import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy to prevent ModuleNotFoundError
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import app # noqa: E402

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    # Mock render_template to avoid needing actual HTML files
    monkeypatch.setattr(app, 'render_template', lambda template_name: b"Home Page")
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home Page" in response.data

def test_predict_invalid_input(client):
    # Since there's no data sent, this should trigger the KeyError and return 400
    response = client.post("/predict")
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
