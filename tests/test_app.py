import pytest
import app as app_module
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'home.html')
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0

def test_predict_route_valid(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'result.html')
    monkeypatch.setattr(app_module.joblib, 'load', lambda path: DummyModel())

    data = {
        'item_weight': '10',
        'item_fat_content': '0',
        'item_visibility': '0.05',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '2',
        'outlet_type': '3'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200

def test_predict_route_invalid_missing_fields(client, monkeypatch):
    data = {
        'item_weight': '10'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 400
    assert b'Invalid input data' in response.data

def test_predict_route_invalid_bad_data(client, monkeypatch):
    data = {
        'item_weight': 'invalid_string',
        'item_fat_content': '0',
        'item_visibility': '0.05',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '2',
        'outlet_type': '3'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 400
    assert b'Invalid input data' in response.data
