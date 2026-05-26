import sys
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()

import app  # noqa: E402


app.model.predict.return_value = [100.0]


def test_invalid_post_returns_400():
    client = app.app.test_client()
    response = client.post('/predict')
    assert response.status_code == 400
