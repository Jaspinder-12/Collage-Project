import pytest
from unittest.mock import patch, MagicMock

import app  # noqa: E402, F401

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    with patch('app.render_template') as mock_render:
        mock_render.return_value = 'Home Page'
        response = client.get('/')
        assert response.status_code == 200
        mock_render.assert_called_with('home.html')

def test_predict(client):
    with patch('app.joblib.load') as mock_load, \
         patch('app.render_template') as mock_render:

        mock_sc = MagicMock()
        mock_sc.transform.return_value = [[0.1] * 9]
        mock_model = MagicMock()
        mock_model.predict.return_value = [1500.50]

        mock_load.side_effect = [mock_sc, mock_model]
        mock_render.return_value = 'Result Page'

        data = {
            'item_weight': '10',
            'item_fat_content': '0',
            'item_visibility': '0.05',
            'item_type': '1',
            'item_mrp': '150',
            'outlet_establishment_year': '1999',
            'outlet_size': '1',
            'outlet_location_type': '1',
            'outlet_type': '1'
        }

        # Test that models are loaded the first time
        app.ml_cache.clear()
        response = client.post('/predict', data=data)
        assert response.status_code == 200
        mock_render.assert_called_with('result.html', prediction=1500.5)
        assert mock_load.call_count == 2

        # Test that models are cached on the second request
        mock_load.reset_mock()
        response2 = client.post('/predict', data=data)
        assert response2.status_code == 200
        assert mock_load.call_count == 0
