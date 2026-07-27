import sys
from unittest.mock import MagicMock

# Mock joblib to prevent actual file loading during tests
sys.modules["joblib"] = MagicMock()

import app  # noqa: E402
import pytest


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index_route(client, mocker):
    mocker.patch("app.render_template", return_value="home")
    response = client.get("/")
    assert response.status_code == 200


def test_predict_route(client, mocker):
    mocker.patch("app.render_template", return_value="result")
    mock_sc = MagicMock()
    mock_sc.transform.return_value = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    mock_model = MagicMock()
    mock_model.predict.return_value = [100.0]

    # Simple mock for joblib.load
    app.joblib.load.side_effect = lambda path: mock_sc if "sc.sav" in str(path) else mock_model

    response = client.post(
        "/predict",
        data={
            "item_weight": "10",
            "item_fat_content": "0",
            "item_visibility": "0.1",
            "item_type": "1",
            "item_mrp": "100",
            "outlet_establishment_year": "1999",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        },
    )

    assert response.status_code == 200
