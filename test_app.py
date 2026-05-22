import sys
from unittest.mock import MagicMock
sys.modules['joblib'] = MagicMock()

import pytest  # noqa: E402
from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict_invalid_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid input provided" in response.data
