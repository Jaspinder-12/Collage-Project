import pytest
import numpy as np


class MockModel:
    def predict(self, X):
        return np.array([42.0])


class MockScaler:
    def transform(self, X):
        return X


def mock_joblib_load(path):
    if "sc.sav" in path:
        return MockScaler()
    return MockModel()


import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict_caching(client, mocker):
    mock_load = mocker.patch("app.joblib.load", side_effect=mock_joblib_load)
    mocker.patch("app.render_template", return_value="mocked")

    data = {
        "item_weight": "1.0",
        "item_fat_content": "1.0",
        "item_visibility": "1.0",
        "item_type": "1.0",
        "item_mrp": "1.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1.0",
        "outlet_location_type": "1.0",
        "outlet_type": "1.0",
    }

    # Clear cache
    app.cache.clear()

    # First request
    client.post("/predict", data=data)
    assert mock_load.call_count == 2

    # Second request
    client.post("/predict", data=data)
    assert mock_load.call_count == 2
