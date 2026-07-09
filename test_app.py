import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_invalid_input(client):
    # Test that missing form data returns 400 instead of crashing with 500
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid input data provided" in response.data
