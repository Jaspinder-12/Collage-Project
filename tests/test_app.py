import pytest
import app as app_module
from app import app
import joblib

class DummyModel:
    def transform(self, X):
        return X
    def predict(self, X):
        return [42.0]

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr(app_module.joblib, "load", lambda path: DummyModel())
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'BigMart Sales Prediction' in response.data
