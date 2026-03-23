import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client


def test_home_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: b"home.html")
    response = client.get("/")
    assert b"home.html" in response.data


def test_predict_route(client, monkeypatch):
    class DummyModel:
        def transform(self, X):
            return X

        def predict(self, X):
            return 42.0

    monkeypatch.setattr(app_module.joblib, "load", lambda *args, **kwargs: DummyModel())
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: b"result.html")

    data = {
        'item_weight': '1',
        'item_fat_content': '1',
        'item_visibility': '1',
        'item_type': '1',
        'item_mrp': '1',
        'outlet_establishment_year': '1',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post("/predict", data=data)
    assert b"result.html" in response.data
