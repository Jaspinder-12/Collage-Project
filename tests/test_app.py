import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a simple byte string to avoid missing template error
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'home.html')
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return 42.0

def test_predict_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'result.html')
    monkeypatch.setattr(app_module.joblib, 'load', lambda path: DummyModel() if 'lr.sav' in path else DummyScaler())

    # Ensure global state is clear
    app_module.sc = None
    app_module.model = None

    data = {
        'item_weight': '10.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'result.html' in response.data

    # Check that caching works
    assert app_module.sc is not None
    assert app_module.model is not None
