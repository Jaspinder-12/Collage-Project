import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a dummy string so we don't need real templates
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: 'mocked template')
    response = client.get('/')
    assert response.status_code == 200
    assert b'mocked template' in response.data

def test_predict_route_invalid_input(client):
    # Missing form fields should return 400 Bad Request
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b'Invalid input' in response.data

    # Invalid type for float casting should return 400 Bad Request
    response = client.post('/predict', data={
        'item_weight': 'invalid',
        'item_fat_content': '0.5',
        'item_visibility': '0.5',
        'item_type': '0.5',
        'item_mrp': '0.5',
        'outlet_establishment_year': '0.5',
        'outlet_size': '0.5',
        'outlet_location_type': '0.5',
        'outlet_type': '0.5'
    })
    assert response.status_code == 400
    assert b'Invalid input' in response.data
