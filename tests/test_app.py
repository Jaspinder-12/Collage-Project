import pytest
import joblib


class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    monkeypatch.setattr(joblib, "load", lambda filepath: DummyModel())


@pytest.fixture(autouse=True)
def mock_render_template(monkeypatch):
    def mock_render(template_name, **kwargs):
        if template_name == "home.html":
            return b"home.html"
        return str(kwargs.get("prediction", 0)).encode("utf-8")

    import app as app_module

    monkeypatch.setattr(app_module, "render_template", mock_render)


@pytest.fixture
def client():
    import app as app_module

    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data


def test_predict_success(client):
    data = {
        "item_weight": "10.0",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "2",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert b"42.0" in response.data


def test_predict_error_handling(client):
    # Missing fields (KeyError)
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data

    # Invalid types (ValueError)
    data = {
        "item_weight": "abc",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "2",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
