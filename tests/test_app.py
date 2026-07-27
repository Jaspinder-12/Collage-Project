import pytest
from app import app
import os

@pytest.fixture
def client(monkeypatch):
    app.config['TESTING'] = True

    # Mock render_template to return template name
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: template_name)

    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

class DummyModel:
    def predict(self, X):
        return [0.0]

class DummyScaler:
    def transform(self, X):
        return X

def test_predict(client, monkeypatch):
    monkeypatch.setattr('app.sc', DummyScaler())
    monkeypatch.setattr('app.model', DummyModel())

    data = {
        'item_weight': '1.0',
        'item_fat_content': '1.0',
        'item_visibility': '1.0',
        'item_type': '1.0',
        'item_mrp': '1.0',
        'outlet_establishment_year': '1.0',
        'outlet_size': '1.0',
        'outlet_location_type': '1.0',
        'outlet_type': '1.0'
    }

    response = client.post('/predict', data=data)
    assert response.status_code == 200
