import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name: b'home.html')
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'result.html')

    class DummyScaler:
        def transform(self, x):
            return x

    class DummyModel:
        def predict(self, x):
            return 42.0

    def dummy_load(path):
        if 'sc.sav' in path:
            return DummyScaler()
        if 'lr.sav' in path:
            return DummyModel()

    monkeypatch.setattr(app_module.joblib, "load", dummy_load)

    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.1',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'result.html' in response.data
