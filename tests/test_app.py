import sys
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import pytest # noqa: E402
import app # noqa: E402


class DummyModel:
    def transform(self, x):
        return x

    def predict(self, x):
        return [42.0]


@pytest.fixture(autouse=True)
def mock_get_model(monkeypatch):
    monkeypatch.setattr(app, 'get_model', lambda x: DummyModel())

@pytest.fixture(autouse=True)
def mock_render_template(monkeypatch):
    monkeypatch.setattr(app, 'render_template', lambda *args, **kwargs: b'mocked render_template')

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'mocked render_template' in response.data

def test_predict(client):
    data = {
        'item_weight': '10',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '2',
        'item_mrp': '100',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    assert b'mocked render_template' in response.data
