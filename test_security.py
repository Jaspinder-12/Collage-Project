import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_debug_mode_disabled():
    assert app.app.debug == False

def test_predict_invalid_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
