import sys
import pytest
from unittest.mock import MagicMock

class MockScaler:
    def transform(self, X):
        return X

class MockModel:
    def predict(self, X):
        return [42.0]

sys.modules['joblib'] = MagicMock()
sys.modules['joblib'].load = lambda path: MockModel() if 'lr.sav' in path else MockScaler()

import app  # noqa: E402

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict(client):
    data = {
        'item_weight': '10',
        'item_fat_content': '0',
        'item_visibility': '0.1',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
