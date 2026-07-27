import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


class DummyScaler:
    def transform(self, X):
        return X


class DummyModel:
    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    def mock_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        if "lr.sav" in filepath:
            return DummyModel()
        return None

    monkeypatch.setattr(sys.modules["joblib"], "load", mock_load)
    app.model_cache = {}  # Reset cache before each test


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda template_name: b"home.html")
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict_success(client, monkeypatch):
    monkeypatch.setattr(
        app, "render_template", lambda template_name, prediction: b"result.html"
    )
    data = {
        "item_weight": "10.5",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "5",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"result.html" in response.data


def test_predict_missing_data(client):
    response = client.post("/predict", data={"item_weight": "10.5"})
    assert response.status_code == 400
    assert b"Invalid input" in response.data


def test_predict_invalid_data(client):
    data = {
        "item_weight": "invalid_string",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "5",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 400
    assert b"Invalid input" in response.data
