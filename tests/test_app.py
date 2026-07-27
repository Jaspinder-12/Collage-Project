import sys
import pytest
from unittest.mock import MagicMock

# Mock joblib and numpy before importing app
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture(autouse=True)
def reset_app_state():
    """Reset model cache before each test to prevent cross-test pollution."""
    app.model_cache = {}
    yield


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    """Test the index route."""
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"mocked index")
    response = client.get("/")
    assert response.status_code == 200
    assert b"mocked index" in response.data


def test_predict(client, monkeypatch):
    """Test the predict route."""
    monkeypatch.setattr(
        app, "render_template", lambda *args, **kwargs: b"mocked result: " + str(kwargs.get("prediction", "")).encode()
    )

    # Mocking the joblib load properly inside the test
    mock_sc = MagicMock()
    mock_sc.transform.return_value = "mocked_X_std"
    mock_model = MagicMock()
    mock_model.predict.return_value = [42.0]

    def mock_joblib_load(path):
        if "sc.sav" in path:
            return mock_sc
        if "lr.sav" in path:
            return mock_model
        return MagicMock()

    sys.modules["joblib"].load = mock_joblib_load

    response = client.post(
        "/predict",
        data={
            "item_weight": "10.0",
            "item_fat_content": "1.0",
            "item_visibility": "0.05",
            "item_type": "2.0",
            "item_mrp": "150.0",
            "outlet_establishment_year": "1999",
            "outlet_size": "2.0",
            "outlet_location_type": "1.0",
            "outlet_type": "1.0",
        },
    )

    assert response.status_code == 200
    assert b"mocked result: 42.0" in response.data
