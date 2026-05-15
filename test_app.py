import pytest
import app  # noqa: E402, F401
from unittest.mock import patch


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict_invalid_input(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input" in response.data


@patch("app.joblib.load")
@patch("app.render_template")
def test_predict_valid_input(mock_render, mock_load, client):
    mock_sc = mock_load.return_value
    mock_sc.transform.return_value = [[0.0] * 9]
    mock_model = mock_load.return_value
    mock_model.predict.return_value = [100.0]
    mock_render.return_value = "Success"

    data = {
        "item_weight": "10.0",
        "item_fat_content": "1.0",
        "item_visibility": "0.1",
        "item_type": "1.0",
        "item_mrp": "100.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1.0",
        "outlet_location_type": "1.0",
        "outlet_type": "1.0",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
