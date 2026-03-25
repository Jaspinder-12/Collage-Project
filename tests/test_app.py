import pytest
import app as app_module
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client, monkeypatch):
    # Mock render_template to return a simple byte string representing the template name
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: template_name.encode('utf-8'))

    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data
