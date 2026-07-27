import pytest
import numpy as np

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return 42.0

@pytest.fixture
def client(monkeypatch):
    import app as main_app

    # Mock render_template to return plain text to avoid needing templates/ for testing
    monkeypatch.setattr(main_app, 'render_template', lambda template, **kwargs: str(kwargs.get('prediction', 'OK')))

    # Inject dummy models into the app module
    main_app.sc = DummyScaler()
    main_app.model = DummyModel()

    with main_app.app.test_client() as client:
        yield client

def test_predict_success(client):
    response = client.post('/predict', data={
        'item_weight': '10.5',
        'item_fat_content': '0',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })

    assert response.status_code == 200
    assert b'42.0' in response.data

def test_predict_models_missing(client, monkeypatch):
    import app as main_app
    main_app.sc = None
    main_app.model = None

    response = client.post('/predict', data={
        'item_weight': '10.5',
        'item_fat_content': '0',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })

    assert response.status_code == 500
    assert b'Models not loaded' in response.data
