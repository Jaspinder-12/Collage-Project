import pytest


class DummyScaler:
    def transform(self, X):
        return X


class DummyModel:
    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    import joblib

    def fake_load(filepath):
        if "sc.sav" in filepath:
            return DummyScaler()
        if "lr.sav" in filepath:
            return DummyModel()
        return None

    monkeypatch.setattr(joblib, "load", fake_load)


@pytest.fixture
def client():
    import app as app_module

    app_module.model_cache = {}
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    import app as app_module

    monkeypatch.setattr(
        app_module,
        "render_template",
        lambda template_name, **context: b"home.html",
    )
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict(client, monkeypatch):
    import app as app_module

    def fake_render(template_name, **context):
        return str(context.get("prediction", "")).encode()

    monkeypatch.setattr(
        app_module,
        "render_template",
        fake_render,
    )

    data = {
        "item_weight": "10.5",
        "item_fat_content": "0",
        "item_visibility": "0.05",
        "item_type": "1",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"42.0" in response.data


def test_predict_error(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
