import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Sales Prediction" in response.data

def test_prediction_endpoint(client):
    """Test the prediction endpoint with dummy data."""
    data = {
        'item_weight': '9.3',
        'item_fat_content': '1',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '249.8',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b"Predicted Sales" in response.data
