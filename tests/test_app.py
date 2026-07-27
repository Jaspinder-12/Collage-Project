import sys
import pytest
from unittest.mock import MagicMock

# Mock joblib and numpy before app import to prevent FileNotFoundError and ModuleNotFoundError
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    """Mock joblib.load to return a dummy model/scaler."""

    class DummyScaler:
        def transform(self, X):
            return X

    class DummyModel:
        def predict(self, X):
            return [42.0]

    def mock_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        return DummyModel()

    monkeypatch.setattr(app.joblib, "load", mock_load)


@pytest.fixture
def client(monkeypatch):
    """A test client for the app."""
    # Reset model cache before each test
    app.model_cache = {}

    # Mock render_template to just return context/string
    def mock_render_template(template_name_or_list, **context):
        if context:
            return f"{template_name_or_list}: {context}"
        return template_name_or_list

    monkeypatch.setattr(app, "render_template", mock_render_template)

    with app.app.test_client() as client:
        yield client


def test_index(client):
    """Test the index route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict(client):
    """Test the predict route."""
    data = {
        "item_weight": "10.5",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "4",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"result.html" in response.data
    assert b"42.0" in response.data


def test_predict_error(client):
    """Test the predict route with invalid data."""
    data = {
        "item_weight": "invalid",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 400
