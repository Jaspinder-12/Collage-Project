import pytest
import numpy as np
import app  # noqa: E402, F401


@pytest.fixture(autouse=True)
def clear_cache():
    app.cache.clear()


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict_route(client, mocker):
    mocker.patch("app.render_template", return_value="Mocked Template")
    mock_sc = mocker.MagicMock()
    mock_sc.transform.return_value = np.array([[1.0]])
    mock_model = mocker.MagicMock()
    mock_model.predict.return_value = np.array([42.5])

    mock_load = mocker.patch("joblib.load", side_effect=[mock_sc, mock_model])

    data = {
        "item_weight": "10.5",
        "item_fat_content": "1.0",
        "item_visibility": "0.1",
        "item_type": "2.0",
        "item_mrp": "150.0",
        "outlet_establishment_year": "1999",
        "outlet_size": "1.0",
        "outlet_location_type": "1.0",
        "outlet_type": "1.0",
    }

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert mock_load.call_count == 2

    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert mock_load.call_count == 2
