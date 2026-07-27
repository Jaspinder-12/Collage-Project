import pytest
from app import app as flask_app
import joblib

class DummyModel:
    def transform(self, X):
        return X
    def predict(self, X):
        return 42.0

@pytest.fixture(autouse=True)
def mock_models(monkeypatch):
    def mock_load(filepath):
        return DummyModel()
    import app as app_module
    monkeypatch.setattr(app_module.joblib, "load", mock_load)
    monkeypatch.setattr(app_module, "render_template", lambda template_name, **context: b"html_content")

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_predict_valid(client):
    data = {
        'item_weight': '1', 'item_fat_content': '1', 'item_visibility': '1',
        'item_type': '1', 'item_mrp': '1', 'outlet_establishment_year': '1',
        'outlet_size': '1', 'outlet_location_type': '1', 'outlet_type': '1'
    }
    rv = client.post('/predict', data=data)
    assert rv.status_code == 200

def test_predict_invalid(client):
    rv = client.post('/predict', data={'item_weight': 'invalid'})
    assert rv.status_code == 400
    assert b"Bad Request" in rv.data
