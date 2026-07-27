import pytest
import app as app_module

@pytest.fixture
def client(monkeypatch):
    app_module.app.config['TESTING'] = True

    # Mock render_template to return context instead of rendering actual template
    def mock_render_template(template_name, **context):
        return f"Template: {template_name}, Context: {context}"
    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    with app_module.app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Template: home.html" in response.data

def test_predict_route_missing_models_fallback(client):
    # Tests the default fallback prediction behavior when tests are running and models are missing
    data = {
        'item_weight': '12.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '150.5',
        'outlet_establishment_year': '1999',
        'outlet_size': '2',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b"Template: result.html" in response.data
    assert b"'prediction': 0.0" in response.data
