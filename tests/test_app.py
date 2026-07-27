import pytest
import app as app_module

@pytest.fixture
def client(monkeypatch):
    app_module.app.config['TESTING'] = True

    # Mock render_template
    def mock_render_template(template_name_or_list, **context):
        return f"Mock rendered: {template_name_or_list}"

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    with app_module.app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mock rendered: home.html" in response.data
