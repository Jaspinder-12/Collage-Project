import pytest
import sys
from unittest.mock import MagicMock

@pytest.fixture(autouse=True)
def mock_dependencies():
    sys.modules['joblib'] = MagicMock()
    sys.modules['numpy'] = MagicMock()
    yield

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"BigMart Sales Prediction" in response.data

@pytest.fixture
def client():
    import app
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client
