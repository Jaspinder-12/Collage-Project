import pytest
import sys
import os

# Add the parent directory to sys.path so we can import app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the index route returns 200 OK."""
    response = client.get('/')
    assert response.status_code == 200
