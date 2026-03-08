import pytest
from app import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda template: f"Mocked {template}")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data

def test_predict_route_missing_fields(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data

def test_predict_route_invalid_fields(client):
    response = client.post('/predict', data={
        'item_weight': 'abc',
        'item_fat_content': '1',
        'item_visibility': '1',
        'item_type': '1',
        'item_mrp': '1',
        'outlet_establishment_year': '1',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    })
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
