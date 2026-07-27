import pytest
import app  # noqa: E402

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    response = client.get("/")
    assert response.status_code == 200
