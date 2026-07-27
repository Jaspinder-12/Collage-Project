import sys
from unittest.mock import MagicMock
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()
import app  # noqa: E402
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
