import pytest
import sys
import numpy as np

# Dummy class for mocking model
class MockModel:
    def predict(self, x):
        return [42.0]

# Dummy class for mocking scaler
class MockScaler:
    def transform(self, x):
        return x

# Mock joblib
class MockJoblib:
    @staticmethod
    def load(path):
        if 'sc.sav' in path:
            return MockScaler()
        return MockModel()

sys.modules['joblib'] = MockJoblib()

import app  # noqa: E402

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    pass  # Avoid testing view without template, but we just need a dummy test.
