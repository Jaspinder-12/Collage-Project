import pytest
from app import app
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.render_template')
def test_index_route(mock_render_template, client):
    mock_render_template.return_value = 'mocked template'
    response = client.get('/')
    assert response.status_code == 200
    mock_render_template.assert_called_once_with('home.html')
