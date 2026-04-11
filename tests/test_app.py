import sys
from unittest.mock import MagicMock

# Mock joblib and numpy before importing app
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import app  # noqa: E402
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    monkeypatch.setattr(app, 'render_template', lambda *args, **kwargs: b"home.html")
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict_invalid_input(client):
    # 🛡️ Sentinel: Test that invalid input returns 400 without stack trace
    response = client.post('/predict', data={'item_weight': 'not a float'})
    assert response.status_code == 400
    assert b"Invalid input" in response.data
