import pytest
import sys
from unittest.mock import MagicMock

# Mock numpy and joblib before importing app
sys.modules["numpy"] = MagicMock()
sys.modules["joblib"] = MagicMock()

import app  # noqa: E402


class DummyScaler:
    def transform(self, X):
        return X


class DummyModel:
    def predict(self, X):
        return [42.0]


@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    def mock_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        if "lr.sav" in filepath:
            return DummyModel()
        return MagicMock()

    app.joblib.load = mock_load

    # Reset model cache for each test
    app.model_cache = {}


@pytest.fixture
def client(monkeypatch):
    app.app.config["TESTING"] = True

    # Mock render_template to prevent jinja2 errors on missing templates
    monkeypatch.setattr(app, "render_template", lambda template_name, **context: b"OK")

    with app.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_predict(client):
    data = {
        "item_weight": "10.5",
        "item_fat_content": "0.0",
        "item_visibility": "0.1",
        "item_type": "1.0",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1.0",
        "outlet_location_type": "2.0",
        "outlet_type": "1.0",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
