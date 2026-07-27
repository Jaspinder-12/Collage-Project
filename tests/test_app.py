import pytest
from app import app
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_predict(client):
    # Ensure dummy models exist for the test
    assert os.path.exists('models/sc.sav')
    assert os.path.exists('models/lr.sav')

    data = {
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
    rv = client.post('/predict', data=data)
    assert rv.status_code == 200
    assert b'Prediction:' in rv.data
