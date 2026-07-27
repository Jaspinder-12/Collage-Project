from app import app, model_cache
import numpy as np


class MockModel:
    def predict(self, x):
        return np.array([42.5])

    def transform(self, x):
        return x


def test_predict_caches_model(mocker):
    mocker.patch("app.joblib.load", side_effect=[MockModel(), MockModel()])
    mocker.patch("app.render_template", return_value="mocked")

    app.config["TESTING"] = True
    with app.test_client() as client:
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
        assert "sc" in model_cache
        assert "model" in model_cache
