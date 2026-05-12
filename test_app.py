import pytest
from unittest.mock import patch, MagicMock
import app  # noqa: E402, F401


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    with patch("app.render_template", return_value="home") as mock_render:
        response = client.get("/")
        assert response.status_code == 200
        mock_render.assert_called_once_with("home.html")


def test_predict(client):
    with patch("app.joblib.load") as mock_load, patch(
        "app.render_template", return_value="result"
    ) as mock_render:
        # Mocking scaler and model
        mock_scaler = MagicMock()
        mock_scaler.transform.return_value = [
            [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        ]
        mock_model = MagicMock()
        mock_model.predict.return_value = [1500.5]

        # joblib.load will return scaler first time, then model second time
        mock_load.side_effect = [mock_scaler, mock_model]

        form_data = {
            "item_weight": "10.5",
            "item_fat_content": "1",
            "item_visibility": "0.05",
            "item_type": "1",
            "item_mrp": "150.0",
            "outlet_establishment_year": "1999",
            "outlet_size": "2",
            "outlet_location_type": "1",
            "outlet_type": "1",
        }

        response = client.post("/predict", data=form_data)

        assert response.status_code == 200
        assert mock_load.call_count == 2
        mock_render.assert_called_once_with("result.html", prediction=1500.5)

        # Second call to verify cache
        mock_load.reset_mock()
        mock_render.reset_mock()

        response2 = client.post("/predict", data=form_data)
        assert response2.status_code == 200
        mock_load.assert_not_called()
        mock_render.assert_called_once_with("result.html", prediction=1500.5)
