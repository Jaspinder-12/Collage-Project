import pytest
import os
import joblib

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return 42.0

@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    def mock_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        return DummyModel()

    # We must import joblib here since app.py uses joblib.load
    monkeypatch.setattr(joblib, 'load', mock_load)

@pytest.fixture
def client(monkeypatch):
    # Import app inside the fixture after joblib is mocked
    import app as app_module
    app_module.app.config['TESTING'] = True

    # Mock render_template to return a dummy string instead of trying to find the HTML template
    def dummy_render_template(template_name, **context):
        if template_name == 'home.html':
            return 'home.html'
        elif template_name == 'result.html':
            return f'result.html - prediction: {context.get("prediction")}'
        return template_name

    monkeypatch.setattr(app_module, 'render_template', dummy_render_template)

    with app_module.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict_valid(client):
    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'result.html' in response.data

def test_predict_missing_data(client):
    data = {
        'item_weight': '10'
        # Missing other fields
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 400
    assert b'Bad Request' in response.data

def test_predict_invalid_data(client):
    data = {
        'item_weight': 'invalid_string',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 400
    assert b'Bad Request' in response.data
