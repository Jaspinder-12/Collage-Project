import pytest
import sys
import numpy as np
from unittest.mock import MagicMock

# Dummy classes for mocking models
class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return 42.0

@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    """
    Mock joblib.load before app is imported because models are loaded at the module level.
    """
    # Create a mock for joblib.load
    def mock_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        if 'lr.sav' in filepath:
            return DummyModel()
        return MagicMock()

    # Apply the mock to the actual joblib module used by the app
    import joblib
    monkeypatch.setattr(joblib, "load", mock_load)

@pytest.fixture
def client():
    # Import app inside the fixture after the mock is applied
    import app as app_module

    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to prevent missing template error
    import app as app_module
    monkeypatch.setattr(app_module, "render_template", lambda template_name, **kwargs: f"mock_{template_name}")

    response = client.get("/")
    assert response.status_code == 200
    assert b"mock_home.html" in response.data

def test_predict_route_success(client, monkeypatch):
    import app as app_module
    monkeypatch.setattr(app_module, "render_template", lambda template_name, **kwargs: f"mock_{template_name}_{kwargs.get('prediction')}")

    data = {
        'item_weight': '10.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"mock_result.html_42.0" in response.data
