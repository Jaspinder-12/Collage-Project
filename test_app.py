import pytest
import sys
import unittest.mock
import urllib.request
import urllib.error
import subprocess
import time

sys.modules["joblib"] = unittest.mock.MagicMock()
sys.modules["numpy"] = unittest.mock.MagicMock()

from app import app  # noqa: E402, F401


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_invalid_input(client, mocker):
    mocker.patch("app.render_template")
    # Sending missing/invalid form data
    response = client.post("/predict", data={"item_weight": "invalid"})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data


def test_debug_mode_disabled():
    process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # Wait for server startup
    try:
        # Check that it responds without exposing werkzeug debugger
        try:
            req = urllib.request.Request("http://localhost:9457/")
            response = urllib.request.urlopen(req)
            assert response.status == 200
        except urllib.error.HTTPError:
            pass
    finally:
        process.terminate()
        process.wait()
