import pytest

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return 42.0

@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    import joblib
    def dummy_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        if 'lr.sav' in filepath:
            return DummyModel()
        return None
    monkeypatch.setattr(joblib, "load", dummy_load)

import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    def dummy_render(template_name, **context):
        return f"Rendered {template_name}".encode()
    monkeypatch.setattr(app_module, 'render_template', dummy_render)
    response = client.get('/')
    assert response.status_code == 200
    assert b'Rendered home.html' in response.data

def test_predict_route_success(client, monkeypatch):
    def dummy_render(template_name, **context):
        pred = context.get("prediction")
        return f"Rendered {template_name} with prediction {pred}".encode()
    monkeypatch.setattr(app_module, 'render_template', dummy_render)

    data = {
        'item_weight': '10',
        'item_fat_content': '0',
        'item_visibility': '0.05',
        'item_type': '4',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'Rendered result.html with prediction 42.0' in response.data

@pytest.fixture(autouse=True)
def reset_model_cache():
    app_module.model_cache = {}
