import pytest
import sys
import os

# Add the project root directory to sys.path so we can import app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"BigMart Sales Prediction" in response.data

def test_predict_route(client):
    # Prepare dummy data matching valid inputs
    # item_fat_content: 0=LF, 1=Low Fat, 2=Regular
    # item_type: 4=Dairy
    # outlet_size: 1=Medium
    # outlet_location_type: 0=Tier 1
    # outlet_type: 1=Supermarket Type1

    data = {
        'item_weight': '9.3',
        'item_fat_content': '1',
        'item_visibility': '0.016047',
        'item_type': '4',
        'item_mrp': '249.8092',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b"Prediction Result" in response.data
    assert b"The predicted sales value is:" in response.data
