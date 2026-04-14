import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy before app import to prevent issues if they are not installed globally in the test environment yet
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import app as app_module

class DummyModel:
    def predict(self, x):
        return 42.0

class DummyScaler:
    def transform(self, x):
        return x

@pytest.fixture(autouse=True)
def setup_mock_model(monkeypatch):
    # Mock joblib.load
    def mock_joblib_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        if 'lr.sav' in filepath:
            return DummyModel()
        return MagicMock()

    monkeypatch.setattr(app_module.joblib, "load", mock_joblib_load)

    # Reset model cache for each test
    app_module.model_cache = {}

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: b'home.html')
    response = client.get("/")
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: b'result.html')
    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '150',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b'result.html' in response.data
