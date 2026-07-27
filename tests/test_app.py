import os
import sys
import pytest

# Ensure the root directory is in the path to import app
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import app as app_module  # noqa: E402


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index_route(client, monkeypatch):
    # Mock render_template to return a dummy string instead of trying to read
    # home.html which might not exist in the environment
    monkeypatch.setattr(
        app_module,
        "render_template",
        lambda template_name, **kwargs: b"mocked_home.html",
    )

    response = client.get("/")
    assert response.status_code == 200
    assert b"mocked_home.html" in response.data


def test_predict_route(client, monkeypatch):
    class DummyScaler:
        def transform(self, X):
            return X

    class DummyModel:
        def predict(self, X):
            return 42.0

    # Mock joblib.load
    def mock_joblib_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        if "lr.sav" in filepath:
            return DummyModel()
        return None

    monkeypatch.setattr(app_module.joblib, "load", mock_joblib_load)

    # Mock render_template
    monkeypatch.setattr(
        app_module,
        "render_template",
        lambda template_name, **kwargs: b"mocked_result.html",
    )

    data = {
        "item_weight": "10",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "2",
        "item_mrp": "100",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }

    response = client.post("/predict", data=data)

    assert response.status_code == 200
    assert b"mocked_result.html" in response.data
