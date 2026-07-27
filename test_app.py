import pytest
from app import app, cache


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_caching(client, mocker):
    mocker.patch("app.render_template", return_value="Mock HTML")
    mocker.patch("joblib.load", side_effect=["mock_sc", "mock_model"])
    mock_scaler = mocker.MagicMock()
    mock_scaler.transform.return_value = "mock_X_std"
    mock_model = mocker.MagicMock()
    mock_model.predict.return_value = [100.0]

    cache["sc"] = mock_scaler
    cache["model"] = mock_model

    response = client.post(
        "/predict",
        data={
            "item_weight": "1",
            "item_fat_content": "1",
            "item_visibility": "1",
            "item_type": "1",
            "item_mrp": "1",
            "outlet_establishment_year": "1",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        },
    )

    assert response.status_code == 200
