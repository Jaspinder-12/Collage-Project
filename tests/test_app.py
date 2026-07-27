import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client, monkeypatch):
    # Mock render_template to return a dummy string instead of looking for templates
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: f"rendered {template_name}")

    response = client.get('/')
    assert response.status_code == 200
    assert b"rendered home.html" in response.data

def test_predict_route_fallback(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: f"rendered {template_name} with prediction {kwargs.get('prediction')}")

    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.1',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b"prediction 0.0" in response.data
