import pytest
from unittest.mock import patch, MagicMock
import app  # noqa: E402, F401


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    with patch("app.render_template") as mock_render:
        mock_render.return_value = "Mocked Home"
        response = client.get("/")
        assert response.status_code == 200
        mock_render.assert_called_with("home.html")


def test_predict_cache(client):
    app.ml_cache.clear()
    with patch("app.render_template") as mock_render, patch("joblib.load") as mock_load:

        mock_render.return_value = "Mocked Result"

        mock_scaler = MagicMock()
        mock_scaler.transform.return_value = [[0]]

        mock_model = MagicMock()
        mock_model.predict.return_value = [42.0]

        mock_load.side_effect = [mock_scaler, mock_model]

        data = {
            "item_weight": "10",
            "item_fat_content": "0",
            "item_visibility": "0.1",
            "item_type": "2",
            "item_mrp": "150",
            "outlet_establishment_year": "1999",
            "outlet_size": "1",
            "outlet_location_type": "0",
            "outlet_type": "1",
        }

        # First request should load models
        resp1 = client.post("/predict", data=data)
        assert resp1.status_code == 200
        assert mock_load.call_count == 2

        # Second request should use cache
        resp2 = client.post("/predict", data=data)
        assert resp2.status_code == 200
        assert mock_load.call_count == 2  # Still 2!

        mock_render.assert_called_with("result.html", prediction=42.0)
