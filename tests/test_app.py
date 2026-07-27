import pytest
import app as app_module
from unittest.mock import MagicMock


class DummyModel:
    def predict(self, X):
        return 42.0


class DummyScaler:
    def transform(self, X):
        return X


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(
        app_module, "render_template", lambda *args, **kwargs: b"home.html"
    )
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict(client, monkeypatch):
    def mock_joblib_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        if "lr.sav" in filepath:
            return DummyModel()
        return MagicMock()

    monkeypatch.setattr(app_module.joblib, "load", mock_joblib_load)
    monkeypatch.setattr(
        app_module,
        "render_template",
        lambda *args, **kwargs: str(kwargs.get("prediction", "")).encode(),
    )

    data = {
        "item_weight": "10.0",
        "item_fat_content": "1",
        "item_visibility": "0.5",
        "item_type": "5",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "0",
        "outlet_type": "1",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"42.0" in response.data
