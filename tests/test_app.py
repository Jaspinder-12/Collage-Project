import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client, monkeypatch):
    """Test that the home page loads successfully"""
    # Mock render_template to return a dummy string so we don't need real templates
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: "Mocked template")

    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Mocked template' in rv.data