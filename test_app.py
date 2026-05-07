import sys
from unittest import mock


class MockModel:
    def predict(self, X):
        return [42.0]


class MockScaler:
    def transform(self, X):
        return X


def mock_load(path):
    if "sc.sav" in path:
        return MockScaler()
    return MockModel()


# Mock joblib before importing app
sys.modules["joblib"] = mock.MagicMock()
sys.modules["joblib"].load = mock.MagicMock(side_effect=mock_load)

import app  # noqa: E402
import pytest  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402


@pytest.fixture
def client(mocker):
    mocker.patch("app.render_template", return_value="Mocked Template")
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_predict_success(client):
    data = {
        "item_weight": "10",
        "item_fat_content": "0",
        "item_visibility": "0.1",
        "item_type": "1",
        "item_mrp": "100",
        "outlet_establishment_year": "1999",
        "outlet_size": "1",
        "outlet_location_type": "1",
        "outlet_type": "1",
    }
    rv = client.post("/predict", data=data)
    assert rv.status_code == 200


def test_predict_invalid_input(client):
    # Missing fields should be caught by Sentinel's try/except block securely
    rv = client.post("/predict", data={})
    assert rv.status_code == 400
    assert b"An error occurred" in rv.data


def test_app_debug_false():
    process = subprocess.Popen([sys.executable, "app.py"])
    try:
        time.sleep(2)
        assert process.poll() is None
    finally:
        process.terminate()
        process.wait()
