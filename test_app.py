import sys
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()

import app  # noqa: E402, F401
import pytest  # noqa: E402


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    app.model.predict.return_value = [100.0]
    with app.app.test_client() as client:
        yield client


def test_predict_missing_data(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
