import sys
from unittest.mock import MagicMock

# Mock numpy and joblib so they don't break on import before we monkeypatch
sys.modules["numpy"] = MagicMock()
sys.modules["joblib"] = MagicMock()

import pytest  # noqa: E402
import app as app_module  # noqa: E402


class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        # Must return a scalar per memory notes
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    # Mock joblib.load to return our DummyModel
    def mock_load(filepath):
        return DummyModel()

    monkeypatch.setattr(app_module.joblib, "load", mock_load)

    # Also mock render_template so we don't depend on HTML files in tests
    monkeypatch.setattr(
        app_module,
        "render_template",
        lambda template_name, **kwargs: b"mocked template",
    )


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"mocked template" in response.data


def test_predict(client):
    # Before the test, clear the cache to ensure isolated test runs
    if hasattr(app_module, "model_cache"):
        app_module.model_cache = {}

    form_data = {
        "item_weight": "10.5",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "4",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "0",
        "outlet_type": "1",
    }

    response = client.post("/predict", data=form_data)
    assert response.status_code == 200
    assert b"mocked template" in response.data
