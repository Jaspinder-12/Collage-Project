import pytest
import app as app_module
from unittest.mock import MagicMock

@pytest.fixture
def client(monkeypatch):
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: template_name)
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict_invalid_input(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: template_name)
    response = client.post('/predict', data={
        'item_weight': 'invalid',
        'item_fat_content': '1',
        'item_visibility': '1',
        'item_type': '1',
        'item_mrp': '1',
        'outlet_establishment_year': '1',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    })
    assert response.status_code == 400
    assert b'Bad Request: Invalid input data' in response.data
