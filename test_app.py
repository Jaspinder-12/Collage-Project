import sys
from unittest.mock import MagicMock
import pytest

sys.modules['joblib'] = MagicMock()

import app # noqa: E402, F401
from app import app as flask_app
from unittest.mock import patch

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

@patch('app.render_template')
def test_index(mock_render_template, client):
    mock_render_template.return_value = 'Mocked Template'
    response = client.get('/')
    assert response.status_code == 200

@patch('app.render_template')
def test_predict(mock_render_template, client):
    mock_render_template.return_value = 'Mocked Template'
    # ⚡ Bolt: Provide a mock prediction value so `float(Y_pred[0])` does not crash with TypeError
    app.model.predict.return_value = [100.0]

    response = client.post('/predict', data={
        'item_weight': '10.5',
        'item_fat_content': '0',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '250.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })
    assert response.status_code == 200