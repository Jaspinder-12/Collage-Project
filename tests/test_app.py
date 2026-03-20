import pytest
import app as app_module
from app import app
import unittest.mock as mock
import numpy as np

class DummyModel:
    def transform(self, X):
        return X
    def predict(self, X):
        return 42.0

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    with mock.patch('app.render_template', return_value="Dummy") as mock_render:
        response = client.get('/')
        assert response.status_code == 200
        mock_render.assert_called_with('home.html')

def test_predict_route(client, monkeypatch):
    monkeypatch.setattr(app_module.joblib, "load", lambda path: DummyModel())
    with mock.patch('app.render_template', return_value="Dummy") as mock_render:
        data = {
            'item_weight': '1', 'item_fat_content': '1', 'item_visibility': '1',
            'item_type': '1', 'item_mrp': '1', 'outlet_establishment_year': '1',
            'outlet_size': '1', 'outlet_location_type': '1', 'outlet_type': '1'
        }
        response = client.post('/predict', data=data)
        assert response.status_code == 200
        mock_render.assert_called_with('result.html', prediction=42.0)
