import pytest
from app import app as main_app
from bs4 import BeautifulSoup
import app

@pytest.fixture
def client(monkeypatch):
    main_app.config['TESTING'] = True
    # mock render_template since we don't have the templates folder
    monkeypatch.setattr(app, 'render_template', lambda template_name, **kwargs: f"Mock rendered {template_name}")
    with main_app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_route_missing_fields(client):
    # This should handle 400 Bad Request since the inputs are not passed
    response = client.post('/predict', data={})
    assert response.status_code == 400
