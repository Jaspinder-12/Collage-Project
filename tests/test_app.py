import pytest
import app as app_module
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: template_name)
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'home.html'

def test_predict_route_bad_request(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: template_name)
    response = client.post('/predict', data={
        # Missing or invalid data to trigger 400 Bad Request
        'item_weight': 'invalid'
    })
    assert response.status_code == 400
    assert b'Bad Request' in response.data
