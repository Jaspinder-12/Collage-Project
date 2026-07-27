import pytest
import sys
from unittest.mock import MagicMock

# Mock dependencies before importing app to avoid FileNotFoundError during test collection
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    mock_load = MagicMock()
    mock_model = MagicMock()
    mock_model.transform.return_value = [[0]]
    mock_model.predict.return_value = [100.0]
    mock_load.return_value = mock_model

    # We also mock the global module so app.py calls use this
    monkeypatch.setattr(app.joblib, "load", mock_load)


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"mocked index")
    response = client.get("/")
    assert response.status_code == 200
    assert b"mocked index" in response.data


def test_predict_success(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"mocked result")
    data = {
        "item_weight": "10.5",
        "item_fat_content": "0",
        "item_visibility": "0.1",
        "item_type": "1",
        "item_mrp": "50.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "0",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"mocked result" in response.data


def test_predict_invalid_input(client):
    data = {
        "item_weight": "invalid",  # this will cause ValueError when converted to float
        "item_fat_content": "0",
        "item_visibility": "0.1",
        "item_type": "1",
        "item_mrp": "50.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "0",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 400
    assert b"Invalid input data" in response.data


def test_predict_missing_input(client):
    data = {
        "item_weight": "10.5"
        # Missing other required fields
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
