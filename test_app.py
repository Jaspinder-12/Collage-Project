import pytest
import sys
import numpy as np

class MockModel:
    def predict(self, X):
        return np.array([42.0])

class MockScaler:
    def transform(self, X):
        return X

class MockJoblib:
    def load(self, path):
        if 'lr.sav' in path:
            return MockModel()
        return MockScaler()

sys.modules['joblib'] = MockJoblib()

import app  # noqa: E402

@pytest.fixture
def client(mocker):
    mocker.patch('app.render_template', return_value='Rendered')
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_predict(client):
    data = {
        'item_weight': '1.0',
        'item_fat_content': '2.0',
        'item_visibility': '3.0',
        'item_type': '4.0',
        'item_mrp': '5.0',
        'outlet_establishment_year': '6.0',
        'outlet_size': '7.0',
        'outlet_location_type': '8.0',
        'outlet_type': '9.0'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert response.data == b'Rendered'
    assert 'sc' in app._model_cache
    assert 'model' in app._model_cache
