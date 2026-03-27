import pytest
import app as app_module
from unittest.mock import patch
import joblib

def test_home_route():
    with patch('app.render_template') as mock_render:
        mock_render.return_value = "Mocked Home"
        with app_module.app.test_client() as client:
            response = client.get('/')
            assert response.status_code == 200

def test_predict_route(monkeypatch):
    class DummyModel:
        def transform(self, X): return X
        def predict(self, X): return 42.0

    monkeypatch.setattr(app_module.joblib, "load", lambda path: DummyModel())

    with patch('app.render_template') as mock_render:
        mock_render.return_value = "Mocked Result"
        with app_module.app.test_client() as client:
            response = client.post('/predict', data={
                'item_weight': '1', 'item_fat_content': '1', 'item_visibility': '1',
                'item_type': '1', 'item_mrp': '1', 'outlet_establishment_year': '1',
                'outlet_size': '1', 'outlet_location_type': '1', 'outlet_type': '1'
            })
            assert response.status_code == 200

    # Teardown global state
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)
