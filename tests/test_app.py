import pytest
import app as app_module

@pytest.fixture
def client(monkeypatch):
    # Mock render_template to return a dummy string
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: "Mocked template")
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mocked template" in response.data
