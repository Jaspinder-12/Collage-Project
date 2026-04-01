import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# --- MOCKING DEPENDENCIES BEFORE IMPORT ---
# We must mock flask, joblib, and numpy because they are likely not installed in this environment.
flask_mock = MagicMock()


# Define a pass-through decorator for app.route
def route_mock(rule, **options):
    def decorator(f):
        return f

    return decorator


# Configure Flask mock instance to return our route decorator
# When app = Flask(__name__) is called, it returns a mock (let's call it app_mock).
# app_mock.route needs to be a side_effect that returns the decorator.
app_mock = MagicMock()
app_mock.route.side_effect = route_mock
flask_mock.Flask.return_value = app_mock

sys.modules["flask"] = flask_mock

joblib_mock = MagicMock()
sys.modules["joblib"] = joblib_mock

numpy_mock = MagicMock()
sys.modules["numpy"] = numpy_mock
# ------------------------------------------

# Set up path to import app from parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the app module
import app  # noqa: E402


class TestApp(unittest.TestCase):

    @patch("app.render_template")
    @patch("app.request")
    @patch("app.joblib.load")
    @patch("app.os.path.exists")
    def test_predict_flow(
        self, mock_exists, mock_load, mock_request, mock_render_template
    ):
        """Test the successful prediction flow with mocked models."""

        # Configure Request
        # Note: We configure the 'mock_request' which replaces 'app.request'
        mock_request.method = "POST"
        mock_request.form = {
            "item_weight": "10.5",
            "item_fat_content": "1",
            "item_visibility": "0.05",
            "item_type": "4",
            "item_mrp": "150.0",
            "outlet_establishment_year": "2000",
            "outlet_size": "1",
            "outlet_location_type": "2",
            "outlet_type": "1",
        }

        # Configure Filesystem Check
        mock_exists.return_value = True  # Simulate models exist

        # Configure Joblib Loading
        mock_scaler = MagicMock()
        mock_model = MagicMock()
        mock_load.side_effect = [mock_scaler, mock_model]

        # Configure Model Prediction
        mock_model.predict.return_value = [2000.123]

        # Run the function
        app.result()

        # Verification
        self.assertEqual(mock_load.call_count, 2)
        mock_scaler.transform.assert_called()
        mock_model.predict.assert_called()
        mock_render_template.assert_called_with("result.html", prediction="2000.12")

    @patch("app.request")
    @patch("app.os.path.exists")
    def test_predict_models_missing(self, mock_exists, mock_request):
        """Test that missing model files result in a 500 error."""

        # Configure Request
        mock_request.method = "POST"
        mock_request.form = {
            "item_weight": "10.5",
            "item_fat_content": "1",
            "item_visibility": "0.05",
            "item_type": "4",
            "item_mrp": "150.0",
            "outlet_establishment_year": "2000",
            "outlet_size": "1",
            "outlet_location_type": "2",
            "outlet_type": "1",
        }

        # Simulate models DO NOT exist
        mock_exists.return_value = False

        # Run the function
        response, status = app.result()

        # Verify
        self.assertEqual(status, 500)
        self.assertIn("Model files not found", response)

    @patch("app.request")
    def test_invalid_input(self, mock_request):
        """Test that invalid numeric input results in a 400 error."""

        # Configure Request
        mock_request.method = "POST"
        mock_request.form = {
            "item_weight": "NOT_A_NUMBER",
        }

        # Run the function
        response, status = app.result()

        # Verify
        self.assertEqual(status, 400)
        self.assertIn("Invalid input", response)


if __name__ == "__main__":
    unittest.main()
