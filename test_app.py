import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_invalid_input(client):
    # Send an incomplete form to trigger a KeyError or ValueError
    response = client.post("/predict", data={"item_weight": "invalid"})
    assert response.status_code == 400
    assert b"error" in response.data


def test_debug_mode_disabled():
    assert not app.debug
