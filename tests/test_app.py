import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and numpy BEFORE importing app to prevent FileNotFoundError and ModuleNotFoundError
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda template_name, **kwargs: b"Mocked Home")
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mocked Home" in response.data


def test_predict(client, monkeypatch):
    app.model_cache = {}  # Reset cache
    monkeypatch.setattr(app, "render_template", lambda template_name, **kwargs: str(kwargs.get("prediction", "")).encode())

    # Mock sc and model
    mock_sc = MagicMock()
    mock_sc.transform.return_value = "transformed_data"
    mock_model = MagicMock()
    mock_model.predict.return_value = [42.0]

    def mock_joblib_load(filepath):
        if "sc.sav" in filepath:
            return mock_sc
        if "lr.sav" in filepath:
            return mock_model

    # Needs to be mocked on the original joblib import within the app
    monkeypatch.setattr(app.joblib, "load", mock_joblib_load)

    response = client.post(
        "/predict",
        data={
            "item_weight": "10.5",
            "item_fat_content": "0",
            "item_visibility": "0.1",
            "item_type": "2",
            "item_mrp": "100.0",
            "outlet_establishment_year": "1999",
            "outlet_size": "1",
            "outlet_location_type": "0",
            "outlet_type": "1",
        },
    )

    assert response.status_code == 200
    assert b"42.0" in response.data
