import pytest
import app as app_module

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_home_route(client, monkeypatch):
    """Test that the home route returns a 200 OK and renders the template."""
    # Mock render_template to avoid needing the templates directory
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: template_name.encode())

    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

def test_predict_route_missing_fields(client, monkeypatch):
    """Test that the predict route handles missing fields appropriately."""
    # Mock joblib.load to return dummy scaler and model
    def mock_joblib_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        elif 'lr.sav' in filepath:
            return DummyModel()
        return None

    monkeypatch.setattr(app_module.joblib, 'load', mock_joblib_load)

    # Need to reset the global state to ensure our mock is used
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

    response = client.post('/predict', data={})
    assert response.status_code == 400

class DummyModel:
    def predict(self, X):
        return 42.0

class DummyScaler:
    def transform(self, X):
        return X

def test_predict_route_success(client, monkeypatch):
    """Test that the predict route handles a successful prediction."""
    # Mock joblib.load to return dummy scaler and model
    def mock_joblib_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        elif 'lr.sav' in filepath:
            return DummyModel()
        return None

    monkeypatch.setattr(app_module.joblib, 'load', mock_joblib_load)

    # Mock render_template to avoid needing the templates directory
    def mock_render_template(template_name, **context):
        # We can assert the context if needed, but for now just return the template name
        return template_name.encode() + b" prediction=" + str(context.get('prediction', '')).encode()

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    # Need to reset the global state to ensure our mock is used
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

    data = {
        'item_weight': '10.0',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '100.0',
        'outlet_establishment_year': '2000',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'result.html' in response.data
    assert b'prediction=42.0' in response.data
