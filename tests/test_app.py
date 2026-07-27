import pytest
from app import app as main_app

@pytest.fixture
def client():
    main_app.config['TESTING'] = True
    with main_app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda template_name: f"Mocked {template_name}")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data
