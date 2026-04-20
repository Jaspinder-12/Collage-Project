import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib before importing app to prevent FileNotFoundError
sys.modules["joblib"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"Mock Home")
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mock Home" in response.data


def test_predict(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"Mock Result")

    # Mocking the joblib load to return a dummy model
    dummy_sc = MagicMock()
    dummy_sc.transform.return_value = [[0] * 9]

    dummy_model = MagicMock()
    dummy_model.predict.return_value = [42.0]

    def mock_load(path):
        if "sc.sav" in path:
            return dummy_sc
        if "lr.sav" in path:
            return dummy_model

    sys.modules["joblib"].load.side_effect = mock_load

    # Clear cache before testing
    app.model_cache = {}

    data = {
        "item_weight": "10",
        "item_fat_content": "1",
        "item_visibility": "0.1",
        "item_type": "1",
        "item_mrp": "100",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"Mock Result" in response.data
