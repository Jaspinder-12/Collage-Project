import sys
from unittest.mock import MagicMock
import pytest

# Mock modules to prevent import failures in testing environment
sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import app as app_module  # noqa: E402

@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    """Mock external dependencies and reset app state."""
    # Reset model cache before each test
    app_module.model_cache = {}

    # Mock joblib load to return mock models
    mock_model = MagicMock()
    mock_model.predict.return_value = [42.0]

    mock_scaler = MagicMock()
    mock_scaler.transform.return_value = [[0]]

    def mock_load(path):
        if 'sc.sav' in path:
            return mock_scaler
        return mock_model

    monkeypatch.setattr(app_module.joblib, 'load', mock_load)

    # Mock render_template to return context data instead of parsing real HTML
    monkeypatch.setattr(app_module, 'render_template', lambda template_name, **context: str(context))

    yield

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_predict(client):
    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '100',
        'outlet_establishment_year': '2000',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert '42.0' in response.get_data(as_text=True)
