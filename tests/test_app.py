import pytest
import os
import joblib

class DummyModel:
    def predict(self, X):
        return 42.0

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    def mock_load(filepath):
        if 'lr' in filepath:
            return DummyModel()
        if 'sc' in filepath:
            return DummyScaler()
    monkeypatch.setattr(joblib, "load", mock_load)

import app as app_module

@pytest.fixture(autouse=True)
def mock_render_template(monkeypatch):
    monkeypatch.setattr(app_module, "render_template", lambda template_name, **kwargs: template_name.encode())

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_cache():
    app_module.model_cache = {}

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data

def test_predict(client):
    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '150',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"result.html" in response.data
