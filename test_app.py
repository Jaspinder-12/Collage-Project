import pytest
from unittest.mock import patch, MagicMock
import app  # noqa: E402, F401

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_predict_invalid_input(client):
    response = client.post('/predict', data={'item_weight': 'invalid'})
    assert response.status_code == 400
    assert b"400 Bad Request" in response.data

@patch('app.joblib.load')
@patch('app.render_template')
def test_predict_valid_input(mock_render_template, mock_joblib_load, client):
    mock_sc = MagicMock()
    mock_sc.transform.return_value = [[0] * 9]
    mock_model = MagicMock()
    mock_model.predict.return_value = [100.5]

    def side_effect(path):
        if 'sc.sav' in path:
            return mock_sc
        return mock_model

    mock_joblib_load.side_effect = side_effect
    mock_render_template.return_value = "Success"

    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
