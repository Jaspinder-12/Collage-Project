import pytest
from app import app

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True
    monkeypatch.setattr('app.render_template', lambda *args, **kwargs: 'mocked')
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_predict_missing_data(client):
    rv = client.post('/predict', data={})
    assert rv.status_code == 400
    assert b"Bad Request: Missing or invalid input data" in rv.data

def test_predict_invalid_data(client):
    rv = client.post('/predict', data={
        'item_weight': 'invalid',
        'item_fat_content': '1',
        'item_visibility': '1',
        'item_type': '1',
        'item_mrp': '1',
        'outlet_establishment_year': '1',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    })
    assert rv.status_code == 400
    assert b"Bad Request: Missing or invalid input data" in rv.data

def test_predict_valid_data(client):
    rv = client.post('/predict', data={
        'item_weight': '1',
        'item_fat_content': '1',
        'item_visibility': '1',
        'item_type': '1',
        'item_mrp': '1',
        'outlet_establishment_year': '1',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    })
    assert rv.status_code == 200
