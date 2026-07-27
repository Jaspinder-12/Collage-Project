import pytest
import time
import subprocess
import urllib.request
import urllib.error
from app import app as flask_app
import app  # noqa: E402, F401


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_predict_invalid_input(client):
    response = client.post(
        "/predict",
        data={
            "item_weight": "invalid",
            "item_fat_content": "1",
            "item_visibility": "1",
            "item_type": "1",
            "item_mrp": "1",
            "outlet_establishment_year": "2000",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        },
    )
    assert response.status_code == 400
    assert b"Invalid input provided" in response.data


def test_server_startup():
    process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # Give the server time to start

    try:
        urllib.request.urlopen("http://127.0.0.1:9457/")
    except urllib.error.HTTPError:
        pass  # Server is up but might return 404/500
    except urllib.error.URLError:
        pytest.fail("Server failed to start or is not reachable.")
    finally:
        process.terminate()
