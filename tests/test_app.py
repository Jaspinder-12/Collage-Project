import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    # Mock render_template to avoid needing the actual HTML file
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"Mocked Home")
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mocked Home" in response.data


def test_predict_invalid_input(client):
    # Send empty data, which should trigger the try/except block
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert response.data == b"Invalid input data"


def test_predict_malformed_input(client):
    # Send non-float data
    response = client.post(
        "/predict",
        data={
            "item_weight": "not a float",
            "item_fat_content": "0.0",
            "item_visibility": "0.0",
            "item_type": "0.0",
            "item_mrp": "0.0",
            "outlet_establishment_year": "0.0",
            "outlet_size": "0.0",
            "outlet_location_type": "0.0",
            "outlet_type": "0.0",
        },
    )
    assert response.status_code == 400
    assert response.data == b"Invalid input data"
