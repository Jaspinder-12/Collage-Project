import sys
import unittest.mock

sys.modules['joblib'] = unittest.mock.MagicMock()

import app  # noqa: E402, F401
import pytest


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_predict_missing_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400