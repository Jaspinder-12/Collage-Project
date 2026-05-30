import sys
from unittest.mock import MagicMock

# Mock joblib to avoid failing on missing ML model files during test collection
sys.modules['joblib'] = MagicMock()

import pytest
from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict_bad_request(client):
    # Test sending no form data, which should raise a KeyError or 400
    response = client.post('/predict', data={})
    assert response.status_code == 400
