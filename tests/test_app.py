import pytest
import app as app_module
from app import app

@pytest.fixture
def client(monkeypatch):
    # Mock render_template
    def mock_render_template(template_name, **context):
        return f"Mocked {template_name}"

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data

def test_predict_invalid_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid input data" in response.data
