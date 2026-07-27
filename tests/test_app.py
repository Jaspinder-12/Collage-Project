import pytest
import app as app_module
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: f"Mocked {template_name_or_list}")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data

def test_predict_invalid_input(client):
    response = client.post('/predict', data={
        'item_weight': 'not a float',
        'item_fat_content': '0',
        'item_visibility': '0',
        'item_type': '0',
        'item_mrp': '0',
        'outlet_establishment_year': '0',
        'outlet_size': '0',
        'outlet_location_type': '0',
        'outlet_type': '0'
    })
    assert response.status_code == 400
    assert b"Bad Request: Invalid or missing form data." in response.data

def test_predict_missing_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Bad Request: Invalid or missing form data." in response.data
