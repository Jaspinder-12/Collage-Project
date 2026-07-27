import sys
from unittest.mock import MagicMock


class MockScaler:
    def transform(self, x):
        return x


class MockModel:
    def predict(self, x):
        return [42.0]


mock_joblib = MagicMock()
mock_joblib.load.side_effect = lambda path: MockScaler() if "sc.sav" in path else MockModel()
sys.modules["joblib"] = mock_joblib

import pytest  # noqa: E402
import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict(client):
    response = client.post(
        "/predict",
        data={
            "item_weight": "1",
            "item_fat_content": "1",
            "item_visibility": "1",
            "item_type": "1",
            "item_mrp": "1",
            "outlet_establishment_year": "1",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        },
    )
    assert response.status_code == 200
