import sys
import pytest
from unittest.mock import MagicMock

# Mock joblib and numpy to avoid loading actual ML models in CI
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client(monkeypatch):
    app.app.config["TESTING"] = True

    # Mock render_template to test without actual templates
    monkeypatch.setattr(app, "render_template", lambda template_name, **kwargs: b"MOCKED_TEMPLATE")

    with app.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_predict_invalid_input(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input provided." in response.data


def test_predict_valid_input(client, monkeypatch):
    # Mock scikit-learn model loading behavior
    mock_model = MagicMock()
    mock_model.predict.return_value = [1234.56]

    mock_sc = MagicMock()
    mock_sc.transform.return_value = [[1, 2, 3]]

    def mock_joblib_load(path):
        if "sc.sav" in path:
            return mock_sc
        return mock_model

    monkeypatch.setattr(app.joblib, "load", mock_joblib_load)

    # Simulate valid form request
    form_data = {
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

    response = client.post("/predict", data=form_data)
    assert response.status_code == 200
