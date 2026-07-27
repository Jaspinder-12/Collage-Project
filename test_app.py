import pytest
from app import app, model_cache
import joblib


class MockModel:
    def predict(self, X):
        return [42.0]


class MockScaler:
    def transform(self, X):
        return X


def test_cache(mocker):
    # clear cache before test
    model_cache.clear()

    mock_load = mocker.patch("joblib.load", side_effect=[MockScaler(), MockModel()])
    mocker.patch("app.render_template", return_value="mocked")

    with app.test_client() as client:
        # First request should load models
        response = client.post(
            "/predict",
            data={
                "item_weight": "1.0",
                "item_fat_content": "1.0",
                "item_visibility": "1.0",
                "item_type": "1.0",
                "item_mrp": "1.0",
                "outlet_establishment_year": "1.0",
                "outlet_size": "1.0",
                "outlet_location_type": "1.0",
                "outlet_type": "1.0",
            },
        )
        assert response.status_code == 200
        assert mock_load.call_count == 2

        # Second request should use cache
        response = client.post(
            "/predict",
            data={
                "item_weight": "1.0",
                "item_fat_content": "1.0",
                "item_visibility": "1.0",
                "item_type": "1.0",
                "item_mrp": "1.0",
                "outlet_establishment_year": "1.0",
                "outlet_size": "1.0",
                "outlet_location_type": "1.0",
                "outlet_type": "1.0",
            },
        )
        assert response.status_code == 200
        assert mock_load.call_count == 2  # still 2, loaded from cache
