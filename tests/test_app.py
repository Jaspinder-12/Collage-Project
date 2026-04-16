import sys
from unittest.mock import MagicMock
import pytest

# Mock modules before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    # Mock joblib.load
    def mock_load(filepath):
        if "sc.sav" in filepath:
            mock_scaler = MagicMock()
            mock_scaler.transform.return_value = [[0.1] * 9]
            return mock_scaler
        elif "lr.sav" in filepath:
            mock_model = MagicMock()
            mock_model.predict.return_value = [1000.0]
            return mock_model
        return MagicMock()

    mocker.patch("joblib.load", side_effect=mock_load)

    # Mock render_template to avoid needing actual HTML files
    mocker.patch("app.render_template", return_value=b"Mocked Template")


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_predict_valid_input(client):
    data = {
        "item_weight": "10.5",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "2",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200


def test_predict_invalid_input(client):
    # Missing fields
    data = {"item_weight": "10.5"}
    response = client.post("/predict", data=data)
    assert response.status_code == 400
    assert b"Invalid input" in response.data or b"Bad Request" in response.data or response.status_code == 400

    # Invalid type
    data = {
        "item_weight": "abc",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "2",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 400
