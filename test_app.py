import pytest
import numpy as np
import sys


# Mock models and scaler
class MockScaler:
    def transform(self, X):
        return X


class MockModel:
    def predict(self, X):
        return np.array([42.0])


class MockJoblib:
    def load(self, path):
        if "sc.sav" in path:
            return MockScaler()
        return MockModel()


sys.modules["joblib"] = MockJoblib()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_predict(client):
    rv = client.post(
        "/predict",
        data={
            "item_weight": "10.0",
            "item_fat_content": "1.0",
            "item_visibility": "0.1",
            "item_type": "1.0",
            "item_mrp": "100.0",
            "outlet_establishment_year": "1999",
            "outlet_size": "2.0",
            "outlet_location_type": "1.0",
            "outlet_type": "1.0",
        },
    )
    assert rv.status_code == 200
