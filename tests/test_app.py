import sys
from unittest.mock import MagicMock

# Mock dependencies before import to prevent ModuleNotFoundError
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


def test_index():
    app.app.testing = True
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
