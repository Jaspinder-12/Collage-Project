import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


class DummyModel:
    def predict(self, X):
        return [42.5]

    def transform(self, X):
        return X


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    def mock_load(filepath):
        if "sc.sav" in filepath:
            return DummyModel()
        elif "lr.sav" in filepath:
            return DummyModel()
        return DummyModel()

    monkeypatch.setattr("app.joblib.load", mock_load)


@pytest.fixture(autouse=True)
def reset_cache():
    app.model_cache = {}


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda template_name: b"Home")
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Home"


def test_predict(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda template_name, prediction: f"Prediction: {prediction}".encode())

    data = {
        "item_weight": "10.5",
        "item_fat_content": "0",
        "item_visibility": "0.1",
        "item_type": "5",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"Prediction: 42.5" in response.data
