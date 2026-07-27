import pytest
import app as app_module

@pytest.fixture
def client(monkeypatch):
    # Mock render_template to return a dummy string instead of trying to look up template files
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: 'mocked')
    app = app_module.app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test the root route ('/') to ensure it returns a 200 OK."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b'mocked'
