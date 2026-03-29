import pytest
import os
import joblib

class DummyModel:
    def predict(self, X):
        return [42.0]

class DummyScaler:
    def transform(self, X):
        return X

# Mock joblib.load before importing app to prevent FileNotFoundError
# during module-level execution (though in app.py they are loaded locally inside the route)
@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    def mock_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        return DummyModel()
    monkeypatch.setattr(joblib, "load", mock_load)

import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    def mock_render(template_name, **kwargs):
        return f'Mocked {template_name}'.encode()
    monkeypatch.setattr(app_module, 'render_template', mock_render)
    response = client.get('/')
    assert response.status_code == 200
    assert b'Mocked home.html' in response.data

def test_predict_route_missing_data(client, monkeypatch):
    def mock_render(template_name, **kwargs):
        return f'Mocked {template_name}'.encode()
    monkeypatch.setattr(app_module, 'render_template', mock_render)
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b'Bad Request' in response.data
