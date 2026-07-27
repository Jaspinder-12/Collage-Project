import pytest


class MockModel:
    def predict(self, X):
        import numpy as np

        return np.array([42.0])


class MockScaler:
    def transform(self, X):
        return X


def mock_load(path):
    if "sc.sav" in path:
        return MockScaler()
    elif "lr.sav" in path:
        return MockModel()
    return None


@pytest.fixture
def client(mocker):
    mocker.patch("joblib.load", side_effect=mock_load)
    import app  # noqa: E402

    app.app._cache = {}  # Reset cache before tests
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict_caching(client, mocker):
    mocker.patch("app.render_template", return_value="Template Rendered")

    data = {
        "item_weight": "10",
        "item_fat_content": "0",
        "item_visibility": "0.1",
        "item_type": "1",
        "item_mrp": "100",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }

    # First request
    response = client.post("/predict", data=data)
    assert response.status_code == 200

    # Second request
    response = client.post("/predict", data=data)
    assert response.status_code == 200

    # Verify joblib.load is called exactly twice (once for scaler, once for model)
    import joblib

    assert joblib.load.call_count == 2
