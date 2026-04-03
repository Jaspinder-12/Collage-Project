import pytest


class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    import joblib

    monkeypatch.setattr(joblib, "load", lambda x: DummyModel())


@pytest.fixture
def client():
    from app import app as flask_app
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    import app as app_module

    monkeypatch.setattr(
        app_module, "render_template", lambda template_name, **kwargs: template_name
    )
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict_success(client, monkeypatch):
    import app as app_module

    monkeypatch.setattr(
        app_module, "render_template", lambda template_name, **kwargs: template_name
    )
    data = {
        "item_weight": "10.5",
        "item_fat_content": "1",
        "item_visibility": "0.1",
        "item_type": "5",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "2",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"result.html" in response.data


def test_predict_failure(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Bad Request" in response.data
