import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_home(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: b"home.html")
    response = client.get('/')
    assert response.status_code == 200
    assert b"home.html" in response.data

def test_predict(client, monkeypatch):
    class DummyScaler:
        def transform(self, X):
            return X

    class DummyModel:
        def predict(self, X):
            return 42.0

    def mock_joblib_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        elif 'lr.sav' in filepath:
            return DummyModel()
        return None

    monkeypatch.setattr(app_module.joblib, "load", mock_joblib_load)
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: b"result.html")

    # Need to clear cache to ensure mock is called
    monkeypatch.setattr(app_module, "model_cache", {})

    response = client.post('/predict', data={
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    })

    assert response.status_code == 200
    assert b"result.html" in response.data

    # Verify cache is populated
    assert 'sc' in app_module.model_cache
    assert 'lr' in app_module.model_cache
