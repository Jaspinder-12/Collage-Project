import pytest
from app import app, model_cache


class MockSc:
    def transform(self, X):
        return X


class MockModel:
    def predict(self, X):
        return [123.45]


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_result_endpoint(client, mocker):
    mocker.patch("app.render_template", return_value="mocked")
    mocker.patch(
        "joblib.load", side_effect=lambda p: MockSc() if "sc.sav" in p else MockModel()
    )

    data = {
        "item_weight": "10",
        "item_fat_content": "1",
        "item_visibility": "0.05",
        "item_type": "1",
        "item_mrp": "100",
        "outlet_establishment_year": "2000",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }

    # First request should cache the model
    model_cache.clear()
    res1 = client.post("/predict", data=data)
    assert res1.status_code == 200
    assert "sc" in model_cache
    assert "model" in model_cache

    # Second request should hit the cache
    res2 = client.post("/predict", data=data)
    assert res2.status_code == 200
