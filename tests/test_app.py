import pytest
import app as app_module
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client, monkeypatch):
    # Mock render_template to return a dummy string instead of needing template files
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'home.html')

    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

class DummyModel:
    def predict(self, X):
        return 42.0

class DummyScaler:
    def transform(self, X):
        return X

def dummy_load(path):
    if 'lr.sav' in path:
        return DummyModel()
    elif 'sc.sav' in path:
        return DummyScaler()
    return None

def test_predict_endpoint(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'result.html')
    monkeypatch.setattr(app_module.joblib, 'load', dummy_load)

    response = client.post('/predict', data={
        'item_weight': '9.3',
        'item_fat_content': '0',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '249.8',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })

    assert response.status_code == 200
    assert b'result.html' in response.data
