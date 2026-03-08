import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_route_missing_model(client):
    # Testing mode default 0.0 response
    data = {
        'item_weight': '9.3',
        'item_fat_content': '0',
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

def test_predict_route_bad_request(client):
    data = {
        'item_weight': 'bad_data'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 400
