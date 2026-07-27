import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a simple string
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: b"Mocked Home Page")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked Home Page" in response.data

def test_predict_invalid_input(client):
    # Test that invalid input to /predict returns 400
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
    assert b"400 Bad Request" in response.data
