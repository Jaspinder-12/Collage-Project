import pytest
from app import app as flask_app
import app as app_module

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template since we don't need to actually render the HTML
    monkeypatch.setattr(app_module, 'render_template', lambda *args, **kwargs: "Mocked template")
    response = client.get('/')
    assert response.status_code == 200

def test_predict_missing_data(client):
    # Testing the Sentinel 400 Bad Request error handler
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid or missing input data" in response.data

def test_predict_invalid_data_type(client):
    # Testing the Sentinel 400 Bad Request error handler
    response = client.post('/predict', data={
        'item_weight': 'not a float',
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
    assert b"Invalid or missing input data" in response.data
