

import sys
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()
from app import app  # noqa: E402


def test_predict_missing_form_data():
    client = app.test_client()
    response = client.post('/predict')
    assert response.status_code == 400
