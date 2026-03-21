import pytest
from app import app
import app as app_module

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True

    # Mock render_template to avoid missing templates/home.html
    def dummy_render_template(template_name_or_list, **context):
        return f"Mocked {template_name_or_list}"

    monkeypatch.setattr(app_module, 'render_template', dummy_render_template)

    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict_missing_input(client):
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Bad Request" in response.data

def test_predict_invalid_input(client):
    response = client.post('/predict', data={
        'item_weight': 'abc',
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
    assert b"Bad Request" in response.data
