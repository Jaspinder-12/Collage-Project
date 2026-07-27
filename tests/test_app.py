import pytest
from app import app
import joblib
import os
import numpy as np

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return 42.0

def mock_joblib_load(filepath):
    if "sc.sav" in filepath:
        return DummyScaler()
    elif "lr.sav" in filepath:
        return DummyModel()
    return None

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(joblib, "load", mock_joblib_load)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint_missing_inputs(client):
    # Send empty POST request to /predict (missing required form fields)
    response = client.post('/predict', data={})

    # Assert that the secure error handling catches the KeyError and returns 400
    assert response.status_code == 400
    assert response.json == {"error": "Invalid or missing input parameters"}

def test_predict_endpoint_invalid_inputs(client):
    # Send POST request with invalid non-numeric inputs
    response = client.post('/predict', data={
        "item_weight": "not a float",
        "item_fat_content": "invalid",
        "item_visibility": "0.1",
        "item_type": "0",
        "item_mrp": "100.5",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "3"
    })

    # Assert that the secure error handling catches the ValueError and returns 400
    assert response.status_code == 400
    assert response.json == {"error": "Invalid or missing input parameters"}

def test_predict_endpoint_success(client, monkeypatch):
    # Mock render_template to return a dummy string instead of reading the filesystem
    import app as main_app
    monkeypatch.setattr(main_app, "render_template", lambda template_name, **kwargs: f"Mocked render: {template_name} with prediction {kwargs.get('prediction')}")

    # Send POST request with valid inputs
    response = client.post('/predict', data={
        "item_weight": "12.5",
        "item_fat_content": "1",
        "item_visibility": "0.1",
        "item_type": "5",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1"
    })

    # Assert that the endpoint processes correctly and returns HTML
    assert response.status_code == 200
    assert b"Mocked render: result.html with prediction 42.0" in response.data  # DummyModel returns 42.0
