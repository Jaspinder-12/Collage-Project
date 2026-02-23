import sys
import unittest
from unittest.mock import MagicMock

# Mock dependencies before importing app
mock_numpy = MagicMock()
sys.modules["numpy"] = mock_numpy

mock_joblib = MagicMock()
sys.modules["joblib"] = mock_joblib

mock_flask = MagicMock()

# Setup Flask mock to return the original function from route decorator
def route_side_effect(*args, **kwargs):
    def decorator(f):
        return f
    return decorator

mock_app = MagicMock()
mock_app.route.side_effect = route_side_effect
mock_flask.Flask.return_value = mock_app

# Setup request object
mock_request = MagicMock()
mock_request.form = {
    'item_weight': '10',
    'item_fat_content': '0.1',
    'item_visibility': '0.5',
    'item_type': '1',
    'item_mrp': '100',
    'outlet_establishment_year': '2000',
    'outlet_size': '2',
    'outlet_location_type': '1',
    'outlet_type': '1'
}
mock_flask.request = mock_request
sys.modules["flask"] = mock_flask

# Import app
try:
    import app
except ImportError:
    app = None

class TestPerformance(unittest.TestCase):
    def setUp(self):
        # Reset mock call count before each test to track calls *during* the test
        if hasattr(mock_joblib.load, 'reset_mock'):
            mock_joblib.load.reset_mock()

    def test_load_count(self):
        if app is None:
            self.fail("Could not import app.py")

        print("Initial joblib.load call count (reset in setUp):", mock_joblib.load.call_count)

        # Simulate request 1
        try:
            app.result()
        except Exception as e:
            print(f"Error in request 1: {e}")
            # If the error is due to missing model file path logic (before fix), we might catch it here
            pass

        count_after_req1 = mock_joblib.load.call_count
        print("Count after req 1:", count_after_req1)

        # Simulate request 2
        try:
            app.result()
        except Exception as e:
             print(f"Error in request 2: {e}")
             pass

        count_after_req2 = mock_joblib.load.call_count
        print("Count after req 2:", count_after_req2)

        # With the optimization, the count should stay 0 because models are loaded at import time
        self.assertEqual(count_after_req1, 0, "joblib.load should not be called during request processing")
        self.assertEqual(count_after_req2, 0, "joblib.load should not be called during request processing")

if __name__ == "__main__":
    unittest.main()
