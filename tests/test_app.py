import pytest
from app import app as main_app

@pytest.fixture
def client():
    main_app.config['TESTING'] = True
    with main_app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a dummy string to avoid looking for actual templates
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: "Mocked HTML")
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Mocked HTML"
