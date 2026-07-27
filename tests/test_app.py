import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(app, 'render_template', lambda template_name: 'home')
    response = client.get('/')
    assert response.status_code == 200

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        return [1.0]

def test_predict_route(client, monkeypatch):
    monkeypatch.setattr(app, 'render_template', lambda template_name, prediction: 'result')
    monkeypatch.setattr(app, 'sc', DummyScaler())
    monkeypatch.setattr(app, 'model', DummyModel())
    data = {
        'item_weight': '10.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '5',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
