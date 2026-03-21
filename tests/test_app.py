import pytest
import app as app_module
from flask import template_rendered

@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: template_name_or_list)
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'home.html'

class DummyModel:
    def transform(self, X):
        return X
    def predict(self, X):
        return 42.0

def test_predict_route(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: f"{template_name_or_list} {context}")
    monkeypatch.setattr(app_module.joblib, 'load', lambda path: DummyModel())

    # Teardown: Reset global state
    monkeypatch.setattr(app_module, 'sc', None)
    monkeypatch.setattr(app_module, 'model', None)

    response = client.post('/predict', data={
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })

    assert response.status_code == 200
    assert 'result.html' in response.data.decode('utf-8')
