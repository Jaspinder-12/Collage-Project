import pytest
import multiprocessing
import time
import urllib.request

from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_predict_invalid_input(client):
    response = client.post("/predict", data={"invalid": "data"})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid or missing input parameters"}


def run_app():
    import app

    app.app.run(port=9457, debug=False)


def test_app_debug_false():
    # Verify that the app can start without debug mode and does not fail on startup
    p = multiprocessing.Process(target=run_app)
    p.start()
    time.sleep(2)  # Give the server time to start

    try:
        req = urllib.request.Request("http://127.0.0.1:9457/")
        try:
            with urllib.request.urlopen(req) as response:
                assert response.status in (200, 500)
        except urllib.error.HTTPError as e:
            # We expect a 500 TemplateNotFound because home.html is missing,
            # but the server should still be running and returning HTTP responses.
            assert e.code == 500
    finally:
        p.terminate()
        p.join()
