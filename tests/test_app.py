import pytest
import sys
from unittest.mock import MagicMock

# Mock numpy and joblib before importing app to avoid ModuleNotFoundError
sys.modules["numpy"] = MagicMock()
sys.modules["joblib"] = MagicMock()

import app  # noqa: E402


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    mock_load = MagicMock()
    mock_model = MagicMock()
    mock_model.predict.return_value = [123.45]
    mock_scaler = MagicMock()
    mock_scaler.transform.return_value = [[0] * 9]

    def side_effect(filepath):
        if "sc.sav" in filepath:
            return mock_scaler
        return mock_model

    mock_load.side_effect = side_effect
    monkeypatch.setattr(app.joblib, "load", mock_load)


@pytest.fixture(autouse=True)
def reset_cache():
    app.model_cache = {}


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(
        app,
        "render_template",
        lambda template: b"home.html" if template == "home.html" else b"result",
    )
    rv = client.get("/")
    assert b"home.html" in rv.data


def test_predict(client, monkeypatch):
    monkeypatch.setattr(
        app, "render_template", lambda template, prediction: b"result.html"
    )
    data = {
        "item_weight": "10",
        "item_fat_content": "0",
        "item_visibility": "0.1",
        "item_type": "1",
        "item_mrp": "50",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }
    rv = client.post("/predict", data=data)
    assert b"result.html" in rv.data
