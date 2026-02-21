import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Ensure the current directory is in sys.path so we can import app
sys.path.append(os.getcwd())

# Create a fresh mock for flask
mock_flask = MagicMock()
# Mock the route decorator: app.route('/')(func) -> func
mock_flask.Flask.return_value.route.return_value = lambda f: f
# Mock render_template
mock_flask.render_template.side_effect = lambda name, **kwargs: name

sys.modules['flask'] = mock_flask
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

# Import app after mocking. Ensure it's reloaded if previously imported.
if 'app' in sys.modules:
    del sys.modules['app']
import app

class TestApp(unittest.TestCase):
    def test_result_missing_data(self):
        with patch('app.request') as mock_request:
            mock_request.form = {}

            result = app.result()
            self.assertIsInstance(result, tuple)
            response, status_code = result

            self.assertEqual(status_code, 400)
            self.assertIn("Missing form data", response)

    def test_result_invalid_data(self):
        with patch('app.request') as mock_request:
            mock_request.form = {
                'item_weight': 'abc',
                'item_fat_content': '1.0',
                'item_visibility': '0.1',
                'item_type': '1',
                'item_mrp': '100',
                'outlet_establishment_year': '1999',
                'outlet_size': '1',
                'outlet_location_type': '1',
                'outlet_type': '1'
            }

            result = app.result()
            self.assertIsInstance(result, tuple)
            response, status_code = result

            self.assertEqual(status_code, 400)
            self.assertIn("Invalid data format", response)

    def test_result_success(self):
        # Mocking the success path
        with patch('app.request') as mock_request, \
             patch('app.joblib.load') as mock_load:

            mock_request.form = {
                'item_weight': '1.0',
                'item_fat_content': '1.0',
                'item_visibility': '0.1',
                'item_type': '1',
                'item_mrp': '100',
                'outlet_establishment_year': '1999',
                'outlet_size': '1',
                'outlet_location_type': '1',
                'outlet_type': '1'
            }

            # Mock scaler
            mock_scaler = MagicMock()
            mock_scaler.transform.return_value = [[0]]
            # Mock model
            mock_model = MagicMock()
            # Return something that can be passed to float()
            mock_model.predict.return_value = 123.45

            # joblib.load is called twice: once for scaler, once for model
            mock_load.side_effect = [mock_scaler, mock_model]

            response = app.result()

            self.assertEqual(response, "result.html")

if __name__ == '__main__':
    unittest.main()
