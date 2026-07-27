import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b'home.html')
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data
