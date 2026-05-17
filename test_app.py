import pytest
import sys
from unittest.mock import MagicMock
sys.modules['joblib'] = MagicMock()
import app  # noqa: E402, F401


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_predict_invalid_input(client):
    response = client.post('/predict', data={'invalid': 'data'})
    assert response.status_code == 400
    assert b'Invalid input provided' in response.data


def test_app_debug_false():
    assert not app.app.debug
