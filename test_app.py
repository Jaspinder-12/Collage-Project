import pytest
from app import app
from unittest.mock import patch, MagicMock
import numpy as np


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict(client):
    with patch('app.joblib.load') as mock_load, \
         patch('app.render_template') as mock_render:

        mock_model = MagicMock()
        mock_model.predict.return_value = np.array([100.5])

        mock_sc = MagicMock()
        mock_sc.transform.return_value = [[0.1] * 9]

        def side_effect(path):
            if 'sc.sav' in path:
                return mock_sc
            return mock_model

        mock_load.side_effect = side_effect
        mock_render.return_value = "Success"

        data = {
            'item_weight': '1',
            'item_fat_content': '1',
            'item_visibility': '1',
            'item_type': '1',
            'item_mrp': '1',
            'outlet_establishment_year': '1',
            'outlet_size': '1',
            'outlet_location_type': '1',
            'outlet_type': '1'
        }

        response = client.post('/predict', data=data)

        assert response.status_code == 200
        assert mock_load.call_count == 2

        # Call again to test cache
        response = client.post('/predict', data=data)
        assert mock_load.call_count == 2
