import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    # Mock render_template to return dummy string
    monkeypatch.setattr('app.render_template', lambda template_name: f"Mocked {template_name}")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data

class DummyScaler:
    def transform(self, X):
        return X

class DummyModel:
    def predict(self, X):
        import numpy as np
        return np.array([12.34])

def test_predict_route_with_dummy_models(client, monkeypatch):
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: f"Mocked {template_name} {kwargs.get('prediction', '')}")
    import app as main_app
    monkeypatch.setattr(main_app, 'sc', DummyScaler())
    monkeypatch.setattr(main_app, 'model', DummyModel())

    response = client.post('/predict', data={
        'item_weight': '12.5',
        'item_fat_content': '0',
        'item_visibility': '0.01',
        'item_type': '2',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    })

    assert response.status_code == 200
    assert b"Mocked result.html 12.34" in response.data
