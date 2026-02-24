import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import numpy as np

# Add parent directory to sys.path so app can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.render_template')
    @patch('app.joblib.load')
    def test_predict_success(self, mock_load, mock_render):
        # Mock scaler
        mock_scaler = MagicMock()
        mock_scaler.transform.return_value = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]

        # Mock model
        mock_model = MagicMock()
        # Ensure return value behaves like numpy array
        mock_model.predict.return_value = np.array([123.45])

        # side_effect for multiple calls
        mock_load.side_effect = [mock_scaler, mock_model]

        # Mock render_template to return a dummy string
        mock_render.return_value = "Prediction: 123.45"

        data = {
            'item_weight': '10.5',
            'item_fat_content': '1',
            'item_visibility': '0.05',
            'item_type': '2',
            'item_mrp': '150.0',
            'outlet_establishment_year': '1999',
            'outlet_size': '1',
            'outlet_location_type': '0',
            'outlet_type': '1'
        }

        response = self.app.post('/predict', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction: 123.45', response.data)

        # Verify render_template called with correct arguments
        mock_render.assert_called_with("result.html", prediction=123.45)

    def test_predict_missing_data(self):
        # Missing 'item_weight'
        data = {
            'item_fat_content': '1',
        }
        response = self.app.post('/predict', data=data)
        # Expect 400 (Bad Request) automatically handled by Flask/Werkzeug
        self.assertEqual(response.status_code, 400)

    def test_predict_invalid_data(self):
        # Invalid float
        data = {
            'item_weight': 'not_a_number',
            'item_fat_content': '1',
            'item_visibility': '0.05',
            'item_type': '2',
            'item_mrp': '150.0',
            'outlet_establishment_year': '1999',
            'outlet_size': '1',
            'outlet_location_type': '0',
            'outlet_type': '1'
        }
        response = self.app.post('/predict', data=data)
        # Expect 400 (Bad Request) handled by try-except block
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
