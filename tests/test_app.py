import pytest
from unittest.mock import MagicMock
import sys

# Mock joblib and numpy before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()
import app  # noqa: E402


class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    def mock_load(filepath):
        return DummyModel()

    monkeypatch.setattr(app.joblib, "load", mock_load)


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda template: b"home.html")
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict_success(client, monkeypatch):
    monkeypatch.setattr(
        app, "render_template", lambda template, prediction: b"result.html"
    )
    data = {
        "item_weight": "10.5",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "5",
        "item_mrp": "150.5",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"result.html" in response.data


def test_predict_invalid_input(client):
    data = {
        "item_weight": "invalid",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "5",
        "item_mrp": "150.5",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
