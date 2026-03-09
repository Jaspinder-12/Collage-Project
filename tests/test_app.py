import pytest
import numpy as np
import app

class DummyModel:
    def predict(self, X):
        return np.array([3000.0])

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture
def client(monkeypatch):
    app.app.config['TESTING'] = True

    # Mock render_template to return strings instead of reading files
    monkeypatch.setattr(app, 'render_template', lambda template_name, **kwargs: f"Template: {template_name}, kwargs: {kwargs}")

    # Set mock models so it doesn't try to read actual files or hit the fallback
    monkeypatch.setattr(app, 'model', DummyModel())
    monkeypatch.setattr(app, 'sc', DummyScaler())

    with app.app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b"Template: home.html" in rv.data

def test_predict(client):
    data = {
        'item_weight': '9.3',
        'item_fat_content': '0',
        'item_visibility': '0.016047',
        'item_type': '4',
        'item_mrp': '249.8092',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    rv = client.post('/predict', data=data)
    assert b"Template: result.html" in rv.data
    assert b"prediction': 3000.0" in rv.data

def test_predict_no_model(client, monkeypatch):
    monkeypatch.setattr(app, 'model', None)
    monkeypatch.setattr(app, 'sc', None)

    data = {
        'item_weight': '9.3',
        'item_fat_content': '0',
        'item_visibility': '0.016047',
        'item_type': '4',
        'item_mrp': '249.8092',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    rv = client.post('/predict', data=data)
    assert b"Template: result.html" in rv.data
    assert b"prediction': 0.0" in rv.data
