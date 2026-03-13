import pytest
import app as app_module
from app import app

class DummyModel:
    def predict(self, X):
        return [0.0]

class DummyScaler:
    def transform(self, X):
        return X

@pytest.fixture(autouse=True)
def mock_models(monkeypatch):
    monkeypatch.setattr(app_module, 'model', DummyModel(), raising=False)
    monkeypatch.setattr(app_module, 'sc', DummyScaler(), raising=False)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client, monkeypatch):
    def mock_render_template(template_name, **context):
        return template_name

    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'home.html'

def test_predict_missing_form_data(client):
    response = client.get('/predict')
    assert response.status_code in (400, 500)
