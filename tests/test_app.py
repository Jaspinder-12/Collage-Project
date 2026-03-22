import pytest
import numpy as np

# We import app after setting PYTHONPATH=. in the test command
import app as app_module

class DummyModel:
    def predict(self, X):
        return 42.0

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a dummy string so we don't need real templates
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **kwargs: "Mocked template")

    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked template" in response.data

def test_predict_route(client, monkeypatch):
    # Mock joblib.load for both scaler and model
    def dummy_load(path):
        if 'sc.sav' in path:
            return DummyScaler()
        if 'lr.sav' in path:
            return DummyModel()
        raise FileNotFoundError(f"Unexpected path: {path}")

    monkeypatch.setattr(app_module.joblib, "load", dummy_load)

    # Reset global variables in the module to ensure they are loaded via mock
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

    # Mock render_template
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **kwargs: f"Mocked result: {kwargs.get('prediction')}")

    data = {
        'item_weight': '12.0',
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
    assert b"Mocked result: 42.0" in response.data
