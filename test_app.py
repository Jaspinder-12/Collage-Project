import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_error_handling(client):
    response = client.post("/predict", data={"item_weight": "invalid"})
    assert response.status_code == 400
    assert response.json == {"error": "An error occurred during prediction"}
