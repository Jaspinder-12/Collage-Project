import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_predict(client):
    rv = client.post('/predict', data=dict(
        item_weight='10.0',
        item_fat_content='1',
        item_visibility='0.05',
        item_type='4',
        item_mrp='150.0',
        outlet_establishment_year='1999',
        outlet_size='1',
        outlet_location_type='1',
        outlet_type='1'
    ), follow_redirects=True)
    assert rv.status_code == 200
    assert b"Prediction" in rv.data
