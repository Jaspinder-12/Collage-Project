import sys
from unittest.mock import MagicMock

# Mock joblib before app import to prevent test collection failures when models are missing
sys.modules['joblib'] = MagicMock()

from app import app  # noqa: E402


def test_predict_bad_request():
    app.testing = True
    client = app.test_client()
    # Missing form data to trigger KeyError/ValueError inside try block
    response = client.post('/predict', data={})
    assert response.status_code == 400
