import pytest
from unittest.mock import patch
import app  # noqa: E402, F401

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_predict_invalid_input(client):
    response = client.post('/predict', data={'item_weight': 'invalid'})
    assert response.status_code == 400
    assert b"Invalid input" in response.data

@patch('app.render_template')
@patch('joblib.load')
def test_predict_valid_input(mock_load, mock_render_template, client):
    mock_render_template.return_value = "Success"
    mock_model = mock_load.return_value
    mock_model.predict.return_value = 100.0
    mock_model.transform.return_value = [[0]]
    data = {
        'item_weight': '10.5',
        'item_fat_content': '1.0',
        'item_visibility': '0.05',
        'item_type': '2.0',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999.0',
        'outlet_size': '2.0',
        'outlet_location_type': '1.0',
        'outlet_type': '1.0'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
