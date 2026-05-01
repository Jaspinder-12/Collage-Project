import pytest


class MockModel:
    def predict(self, x):
        return [1000.5]


class MockScaler:
    def transform(self, x):
        return x


import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict_route(client, mocker):
    mock_load = mocker.patch("joblib.load", side_effect=lambda path: MockScaler() if "sc.sav" in path else MockModel())

    response = client.post(
        "/predict",
        data={
            "item_weight": "10",
            "item_fat_content": "0",
            "item_visibility": "0.05",
            "item_type": "1",
            "item_mrp": "100",
            "outlet_establishment_year": "1999",
            "outlet_size": "1",
            "outlet_location_type": "0",
            "outlet_type": "1",
        },
    )
    assert response.status_code == 200
    assert mock_load.call_count == 2

    # Second call should use cache
    response = client.post(
        "/predict",
        data={
            "item_weight": "10",
            "item_fat_content": "0",
            "item_visibility": "0.05",
            "item_type": "1",
            "item_mrp": "100",
            "outlet_establishment_year": "1999",
            "outlet_size": "1",
            "outlet_location_type": "0",
            "outlet_type": "1",
        },
    )
    assert response.status_code == 200
    assert mock_load.call_count == 2  # Still 2!
