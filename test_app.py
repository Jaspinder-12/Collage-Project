import pytest
from app import app

import app as app_module


@pytest.fixture
def client():
    app_module.model_cache = {}
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"BigMart Sales Prediction" in rv.data


def test_predict_success(client):
    # This test should pass when paths are fixed.
    data = {
        "item_weight": "9.3",
        "item_fat_content": "0",
        "item_visibility": "0.016",
        "item_type": "4",
        "item_mrp": "249.8",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "0",
        "outlet_type": "1",
    }
    rv = client.post("/predict", data=data)
    assert rv.status_code == 200
    assert b"Predicted Sales:" in rv.data


def test_predict_invalid_input(client):
    # This test should return 400 when validation is implemented.
    data = {
        "item_weight": "invalid",
        "item_fat_content": "0",
        "item_visibility": "0.016",
        "item_type": "4",
        "item_mrp": "249.8",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "0",
        "outlet_type": "1",
    }
    rv = client.post("/predict", data=data)
    assert rv.status_code == 400
    assert b"Invalid input" in rv.data


def test_predict_missing_input(client):
    # This test should return 400 for missing fields.
    data = {
        "item_weight": "9.3"
        # Missing other fields
    }
    rv = client.post("/predict", data=data)
    assert rv.status_code == 400
    assert b"Missing input" in rv.data
