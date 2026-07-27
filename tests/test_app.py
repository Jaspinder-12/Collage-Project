import pytest
from app import app
import os
import joblib
import numpy as np

class DummyModel:
    def predict(self, X):
        return 42.0

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True

    # Mock models using monkeypatch instead of generating binary files
    monkeypatch.setattr('app.joblib.load', lambda path: DummyScaler() if 'sc.sav' in path else DummyModel())

    # Mock render_template to return arguments instead of rendering
    import app as app_module
    def mock_render_template(template_name, **kwargs):
        return f"{template_name} - {kwargs}"
    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the index route returns the home page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"home.html" in rv.data

def test_predict_route(client):
    """Test the predict route with dummy data."""
    # Helper to create dummy data matching the input form
    data = {
        'item_weight': '9.3',
        'item_fat_content': '1',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '249.8',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }

    rv = client.post('/predict', data=data)
    assert rv.status_code == 200
    assert b"result.html" in rv.data
    assert b"42.0" in rv.data
