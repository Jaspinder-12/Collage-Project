import pytest
from unittest.mock import MagicMock
import sys

# Mock sys.modules for joblib and numpy before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client(monkeypatch):
    app.app.config["TESTING"] = True

    # Mock render_template to avoid needing HTML files in tests
    monkeypatch.setattr(
        app,
        "render_template",
        lambda template_name, **kwargs: template_name.encode()
    )

    with app.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict(client, monkeypatch):
    # Mock joblib.load
    class DummyModel:
        def predict(self, X):
            return 42.0

    class DummyScaler:
        def transform(self, X):
            return X

    def mock_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        elif "lr.sav" in filepath:
            return DummyModel()
        return MagicMock()

    # Apply the mock to the specific module where it's used
    monkeypatch.setattr(app.joblib, "load", mock_load)

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
