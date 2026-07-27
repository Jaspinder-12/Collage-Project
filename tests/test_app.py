import pytest
import app as app_module
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: template_name_or_list)
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'home.html'

def test_predict_route_missing_models(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: template_name_or_list)
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

    data = {
        'item_weight': '10.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert response.data == b'result.html'
