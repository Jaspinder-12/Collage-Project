import pytest
from unittest.mock import MagicMock
import app  # noqa: E402, F401


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_predict_caching(client, mocker):
    mocker.patch("app.render_template", return_value="Success")
    mock_load = mocker.patch("app.joblib.load")

    mock_sc = MagicMock()
    mock_sc.transform.return_value = [
        [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    ]
    mock_model = MagicMock()
    mock_model.predict.return_value = [100.0]

    mock_load.side_effect = [mock_sc, mock_model]

    form_data = {
        "item_weight": "1.0",
        "item_fat_content": "2.0",
        "item_visibility": "3.0",
        "item_type": "4.0",
        "item_mrp": "5.0",
        "outlet_establishment_year": "6.0",
        "outlet_size": "7.0",
        "outlet_location_type": "8.0",
        "outlet_type": "9.0",
    }

    # First request
    response1 = client.post("/predict", data=form_data)
    assert response1.status_code == 200
    assert mock_load.call_count == 2

    # Second request
    response2 = client.post("/predict", data=form_data)
    assert response2.status_code == 200
    # Call count remains 2 due to caching
    assert mock_load.call_count == 2
