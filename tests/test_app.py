import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    with patch('app.render_template') as mock_render:
        mock_render.return_value = "Mocked Response"
        response = client.get('/')
        assert response.status_code == 200

def test_predict_route_missing_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"400 Bad Request" in response.data
