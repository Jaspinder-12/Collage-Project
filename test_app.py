import sys
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()
from app import app  # noqa: E402
import pytest  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict_invalid_post(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
