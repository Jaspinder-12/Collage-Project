import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda *args, **kwargs: 'mock template')
    response = client.get('/')
    assert response.status_code == 200

def test_predict_invalid_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid input" in response.data
