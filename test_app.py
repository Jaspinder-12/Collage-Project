import pytest
from unittest.mock import patch
import app  # noqa: E402, F401

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index_mocked(client):
    with patch('app.render_template', return_value='Mocked'):
        res = client.get('/')
        assert res.status_code == 200

def test_predict_mocked(client):
    with patch('app.render_template', return_value='Mocked Predict'):
        res = client.post('/predict', data={
            'item_weight': '10',
            'item_fat_content': '1',
            'item_visibility': '0.05',
            'item_type': '1',
            'item_mrp': '100',
            'outlet_establishment_year': '1999',
            'outlet_size': '1',
            'outlet_location_type': '1',
            'outlet_type': '1'
        })
        assert res.status_code == 200
