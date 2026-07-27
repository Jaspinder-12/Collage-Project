import pytest
import app as app_module

class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **kwargs: b'home.html')
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict_success(client, monkeypatch):
    monkeypatch.setattr(app_module.joblib, 'load', lambda x: DummyModel())
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **kwargs: b'result.html')
    data = {
        'item_weight': '10.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'result.html' in response.data

def test_predict_invalid_data(client):
    data = {
        'item_weight': 'invalid',
        'item_fat_content': '1'
        # missing other fields
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 400
    assert b'Invalid input data' in response.data
