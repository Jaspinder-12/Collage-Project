import pytest
import joblib
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

class DummyModel:
    def transform(self, X):
        return X
    def predict(self, X):
        return 42.0

@pytest.fixture(autouse=True)
def mock_models(monkeypatch):
    def mock_load(path):
        return DummyModel()
    monkeypatch.setattr(app_module.joblib, 'load', mock_load)

    def mock_render_template(template_name_or_list, **context):
        return f"Mock template: {template_name_or_list}"
    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mock template: home.html" in response.data

def test_predict_route(client):
    form_data = {
        'item_weight': '9.3',
        'item_fat_content': '0',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '249.8',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=form_data)
    assert response.status_code == 200
    assert b"Mock template: result.html" in response.data
