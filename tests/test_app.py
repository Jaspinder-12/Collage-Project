import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a simple string, to avoid needing templates dir
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: 'Mocked Template')

    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Mocked Template'

def test_predict_route_missing_data(client, monkeypatch):
    # Mock render_template in case we hit the return
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: 'Mocked Template')

    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert "Bad Request: Missing or invalid form data" in response.data.decode('utf-8')

def test_predict_route_invalid_data(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: 'Mocked Template')

    response = client.post('/predict', data={
        'item_weight': 'invalid',
        'item_fat_content': '0',
        'item_visibility': '0',
        'item_type': '0',
        'item_mrp': '0',
        'outlet_establishment_year': '0',
        'outlet_size': '0',
        'outlet_location_type': '0',
        'outlet_type': '0'
    })
    assert response.status_code == 400
    assert "Bad Request: Missing or invalid form data" in response.data.decode('utf-8')
