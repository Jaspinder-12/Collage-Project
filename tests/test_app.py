import pytest
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_home_page(client, monkeypatch):
    # Mock render_template to avoid needing the templates directory in tests
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: template_name)
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data
