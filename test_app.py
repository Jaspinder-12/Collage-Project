import pytest
import sys

sys.modules['joblib'] = type('joblib', (), {'load': lambda x: type('Model', (), {'predict': lambda x: [0], 'transform': lambda x: x})()})
from app import app  # noqa: E402

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
