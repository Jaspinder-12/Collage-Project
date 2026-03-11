import pytest
import app

class DummyModel:
    def predict(self, X):
        return [42.0]

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture
def client(monkeypatch):
    app.app.config['TESTING'] = True

    monkeypatch.setattr(app, 'model', DummyModel())
    monkeypatch.setattr(app, 'sc', DummyScaler())

    with app.app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda *args, **kwargs: 'mocked template')
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'mocked template'

def test_predict_valid_input(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda *args, **kwargs: 'mocked template')
    response = client.post('/predict', data={
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.1',
        'item_type': '2',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })
    assert response.status_code == 200
    assert response.data == b'mocked template'

def test_predict_invalid_input(client):
    response = client.post('/predict', data={
        'item_weight': 'invalid',
    })
    assert response.status_code == 400
