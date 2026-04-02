import pytest
import app as app_module

class DummyModel:
    def predict(self, X):
        return 42.0

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    def mock_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        if 'lr.sav' in filepath:
            return DummyModel()
        return None
    monkeypatch.setattr(app_module.joblib, "load", mock_load)

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_model_cache():
    # Reset cache before each test to ensure mocked state isolation
    app_module.model_cache = {}
    yield

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, "render_template", lambda template, **kwargs: f"rendered {template}".encode("utf-8"))
    response = client.get("/")
    assert response.status_code == 200
    assert b"rendered home.html" in response.data

def test_predict_route(client, monkeypatch):
    monkeypatch.setattr(app_module, "render_template", lambda template, **kwargs: f"rendered {template} with pred {kwargs.get('prediction')}".encode("utf-8"))

    data = {
        'item_weight': '12.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '4',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '2',
        'outlet_type': '1'
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"rendered result.html with pred 42.0" in response.data

def test_predict_route_missing_data(client):
    data = {
        'item_weight': '12.5'
        # Missing other fields
    }
    # Standard Flask error handling for missing form data is 400 Bad Request
    response = client.post("/predict", data=data)
    assert response.status_code == 400
