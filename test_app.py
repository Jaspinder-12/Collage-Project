import pytest
import subprocess
import time
import urllib.request
import urllib.error
from unittest.mock import patch
import app  # noqa: E402, F401


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


@patch("app.render_template")
def test_index(mock_render_template, client):
    mock_render_template.return_value = "Mocked Template"
    response = client.get("/")
    assert response.status_code == 200


def test_predict_invalid_input(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data


def test_server_startup():
    process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # Give the server time to start
    try:
        # Basic check to ensure the process is alive
        assert process.poll() is None

        # Attempt to connect to the server
        try:
            urllib.request.urlopen("http://127.0.0.1:9457/")
        except urllib.error.HTTPError as e:
            # Server is up but might return an error due to missing template/route
            assert e.code in [200, 404, 500]
    finally:
        process.terminate()
        process.wait()
