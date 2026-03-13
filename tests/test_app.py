import pytest
from app import app
import app as app_module

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return a dummy string instead of rendering the file
    def mock_render_template(template_name_or_list, **context):
        return f"Mocked {template_name_or_list}"

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data

def test_predict_route_missing_inputs(client, monkeypatch):
    def mock_render_template(template_name_or_list, **context):
        return f"Mocked {template_name_or_list} with prediction {context.get('prediction')}"

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    # Test safe casting returns 400 Bad Request on invalid form
    response = client.post('/predict', data={})
    assert response.status_code == 400
    assert b"Bad Request" in response.data

def test_predict_route_with_dummy_model(client, monkeypatch):
    # Create dummy models to bypass FileNotFoundError issues
    class DummyScaler:
        def transform(self, X):
            return X

    class DummyModel:
        def predict(self, X):
            return [100.0]

    monkeypatch.setattr(app_module, 'sc', DummyScaler())
    monkeypatch.setattr(app_module, 'model', DummyModel())

    def mock_render_template(template_name_or_list, **context):
        return f"Mocked {template_name_or_list} with prediction {context.get('prediction')}"

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '1',
        'item_mrp': '100',
        'outlet_establishment_year': '2000',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b"Mocked result.html with prediction 100.0" in response.data
