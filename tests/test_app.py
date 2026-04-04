import pytest


class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib(monkeypatch):
    import joblib

    def mock_load(filepath):
        return DummyModel()

    monkeypatch.setattr(joblib, "load", mock_load)


@pytest.fixture
def client():
    import app as app_module

    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    import app as app_module

    def mock_render_template(template_name, **kwargs):
        return f"Rendered {template_name}"

    monkeypatch.setattr(app_module, "render_template", mock_render_template)

    response = client.get("/")
    assert response.status_code == 200
    assert b"Rendered home.html" in response.data


def test_predict_invalid_input(client, monkeypatch):
    import app as app_module

    def mock_render_template(template_name, **kwargs):
        return f"Rendered {template_name}"

    monkeypatch.setattr(app_module, "render_template", mock_render_template)

    # Missing form fields should raise KeyError in app.py which is now caught
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data

    # Invalid form fields (strings instead of numbers) should raise ValueError
    response = client.post(
        "/predict",
        data={
            "item_weight": "invalid",
            "item_fat_content": "invalid",
            "item_visibility": "invalid",
            "item_type": "invalid",
            "item_mrp": "invalid",
            "outlet_establishment_year": "invalid",
            "outlet_size": "invalid",
            "outlet_location_type": "invalid",
            "outlet_type": "invalid",
        },
    )
    assert response.status_code == 400
    assert b"Invalid input data" in response.data


def test_predict_valid_input(client, monkeypatch):
    import app as app_module

    def mock_render_template(template_name, **kwargs):
        pred = kwargs.get("prediction")
        return f"Rendered {template_name} with prediction {pred}"

    monkeypatch.setattr(app_module, "render_template", mock_render_template)

    response = client.post(
        "/predict",
        data={
            "item_weight": "1.0",
            "item_fat_content": "1.0",
            "item_visibility": "1.0",
            "item_type": "1.0",
            "item_mrp": "1.0",
            "outlet_establishment_year": "1.0",
            "outlet_size": "1.0",
            "outlet_location_type": "1.0",
            "outlet_type": "1.0",
        },
    )
    assert response.status_code == 200
    assert b"Rendered result.html with prediction 42.0" in response.data
