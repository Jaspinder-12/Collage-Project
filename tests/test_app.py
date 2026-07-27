import sys
from unittest.mock import MagicMock

import os

# Mock dependencies before import to prevent ModuleNotFoundError
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, base)

import app  # noqa: E402


def test_index():
    app.app.testing = True
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
