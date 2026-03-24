import pytest
from app import app as flask_app
import app as app_module

@pytest.fixture
def client(monkeypatch):
    flask_app.config['TESTING'] = True

    # Mock render_template to return a dummy string, avoiding missing template errors in tests
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: b"mocked template")

    with flask_app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200

def test_predict_invalid_data(client):
    """Test that missing or invalid data returns a 400 Bad Request."""
    # Sending missing data
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Invalid or missing input data" in response.data

    # Sending invalid data (string instead of float)
    invalid_data = {
        'item_weight': 'invalid',
        'item_fat_content': 'invalid',
        'item_visibility': 'invalid',
        'item_type': 'invalid',
        'item_mrp': 'invalid',
        'outlet_establishment_year': 'invalid',
        'outlet_size': 'invalid',
        'outlet_location_type': 'invalid',
        'outlet_type': 'invalid'
    }
    response = client.post('/predict', data=invalid_data)
    assert response.status_code == 400
    assert b"Invalid or missing input data" in response.data
