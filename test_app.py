import numpy as np


# Mocking out the joblib and joblib.load so we don't need real models.
class MockModel:
    def predict(self, X):
        return np.array([42.0])


class MockScaler:
    def transform(self, X):
        return X


from unittest.mock import patch  # noqa: E402


@patch("app.joblib.load", side_effect=[MockScaler(), MockModel()])
@patch("app.render_template", return_value="Result")
def test_predict_caching(mock_render_template, mock_load):

    import app

    # Enable test mode so we can use test_client
    app.app.config["TESTING"] = True
    client = app.app.test_client()

    data = {
        "item_weight": "10",
        "item_fat_content": "1",
        "item_visibility": "0.1",
        "item_type": "2",
        "item_mrp": "100",
        "outlet_establishment_year": "1999",
        "outlet_size": "2",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }

    # First request should call joblib.load twice (scaler and model)
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert app.joblib.load.call_count == 2

    # Second request should not call joblib.load again
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert app.joblib.load.call_count == 2  # Still 2
