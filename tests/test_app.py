import sys
from unittest.mock import MagicMock

# Mock external dependencies to prevent ModuleNotFoundError or FileNotFoundError
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import app # noqa: E402

import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    pass
