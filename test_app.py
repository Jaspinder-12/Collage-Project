import sys
from unittest.mock import MagicMock, patch
import pytest

# Mock dependencies that are missing or involve binary files
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()
import numpy  # noqa: E402
numpy.array = MagicMock(return_value=MagicMock())

from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Home" in rv.data


def test_predict_invalid_input(client):
    rv = client.post('/predict', data={'item_weight': 'abc'})
    assert rv.status_code == 400
    assert b"Invalid input" in rv.data


def test_predict_missing_input(client):
    rv = client.post('/predict', data={})
    assert rv.status_code == 400
    assert b"Invalid input" in rv.data


def test_predict_valid_input_no_model(client):
    # This should trigger the 500 error I added for missing models
    # We ensure models dir doesn't have the files by mocking os.path.exists
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        rv = client.post('/predict', data={
            'item_weight': '1.0',
            'item_fat_content': '1.0',
            'item_visibility': '0.01',
            'item_type': '1.0',
            'item_mrp': '100.0',
            'outlet_establishment_year': '1999',
            'outlet_size': '1.0',
            'outlet_location_type': '1.0',
            'outlet_type': '1.0'
        })
        assert rv.status_code == 500
        assert b"model not found" in rv.data


def test_predict_full_success(client):
    # Mock everything to test the full path
    with patch('os.path.exists') as mock_exists, \
         patch('joblib.load') as mock_load, \
         patch('app.render_template') as mock_render:

        mock_exists.return_value = True

        mock_scaler = MagicMock()
        mock_scaler.transform.return_value = MagicMock()

        mock_model = MagicMock()
        mock_model.predict.return_value = [123.45]

        mock_load.side_effect = [mock_scaler, mock_model]
        mock_render.return_value = "Result: 123.45"

        rv = client.post('/predict', data={
            'item_weight': '1.0',
            'item_fat_content': '1.0',
            'item_visibility': '0.01',
            'item_type': '1.0',
            'item_mrp': '100.0',
            'outlet_establishment_year': '1999',
            'outlet_size': '1.0',
            'outlet_location_type': '1.0',
            'outlet_type': '1.0'
        })

        assert rv.status_code == 200
        assert b"Result: 123.45" in rv.data
