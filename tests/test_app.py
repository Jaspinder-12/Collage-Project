import pytest
from app import app
import os
import joblib
import numpy as np

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test that the index route returns the home page."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"BigMart Sales Prediction" in rv.data
    # Check for the UX improvement elements
    assert b'spinner' in rv.data
    assert b'Predicting...' in rv.data

def test_predict_route(client):
    """Test the predict route with dummy data."""
    # Ensure models exist
    assert os.path.exists(os.path.join('models', 'sc.sav'))
    assert os.path.exists(os.path.join('models', 'lr.sav'))

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
    assert b"Prediction Result" in rv.data
    assert b"Predicted Item Outlet Sales:" in rv.data
