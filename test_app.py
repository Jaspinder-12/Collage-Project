import pytest
from unittest.mock import patch, MagicMock
from app import app, model_cache


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_caches_model(client):
    model_cache.clear()

    with patch("app.joblib.load") as mock_load, patch(
        "app.render_template"
    ) as mock_render:
        mock_sc = MagicMock()
        mock_sc.transform.return_value = [[0]]
        mock_model = MagicMock()
        mock_model.predict.return_value = [42.0]

        mock_load.side_effect = [mock_sc, mock_model, mock_sc, mock_model]
        mock_render.return_value = "Result"

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

        _ = client.post("/predict", data=data)
        assert mock_load.call_count == 2

        _ = client.post("/predict", data=data)
        assert mock_load.call_count == 2
