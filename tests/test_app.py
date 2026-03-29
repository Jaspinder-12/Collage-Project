import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **kwargs: f'Mocked {template_name}'.encode())
    response = client.get('/')
    assert response.status_code == 200
    assert b'Mocked home.html' in response.data

def test_predict_route_missing_data(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **kwargs: f'Mocked {template_name}'.encode())
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b'Bad Request' in response.data
