import pytest
import sys
from unittest.mock import MagicMock

# Mock libraries to avoid ModuleNotFoundError or FileNotFoundError
sys.modules["joblib"] = MagicMock()
sys.modules["numpy"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    # Reset cache for test isolation
    app.model_cache = {}
    with app.app.test_client() as client:
        yield client


def test_predict(client, monkeypatch):
    monkeypatch.setattr(app, "render_template", lambda *args, **kwargs: b"Mocked")
    response = client.post(
        "/predict",
        data={
            "item_weight": "1",
            "item_fat_content": "2",
            "item_visibility": "3",
            "item_type": "4",
            "item_mrp": "5",
            "outlet_establishment_year": "6",
            "outlet_size": "7",
            "outlet_location_type": "8",
            "outlet_type": "9",
        },
    )
    assert response.status_code == 200
    assert b"Mocked" in response.data
