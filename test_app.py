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

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_get(client):
    response = client.get('/predict')
    # Since we didn't send form data, we will get KeyError -> 400 Bad Request
    assert response.status_code in [400, 500]
