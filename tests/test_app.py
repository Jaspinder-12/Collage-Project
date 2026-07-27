import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    def mock_render_template(template_name_or_list, **context):
        return "Mock Home Page"
    monkeypatch.setattr('app.render_template', mock_render_template)

    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Mock Home Page"
