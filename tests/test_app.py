import sys
import pytest
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()
sys.modules['numpy'] = MagicMock()

import app as app_module  # noqa: E402


@pytest.fixture(autouse=True)
def setup_teardown():
    app_module.model_cache = {}
    yield


@pytest.fixture
def client():
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: b"mocked_home")
    rv = client.get('/')
    assert b'mocked_home' in rv.data


def test_predict(client, monkeypatch):
    monkeypatch.setattr(app_module, 'render_template', lambda template_name_or_list, **context: b"mocked_result")

    data = {
        'item_weight': '9.3',
        'item_fat_content': '0',
        'item_visibility': '0.016',
        'item_type': '4',
        'item_mrp': '249.8',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '0',
        'outlet_type': '1'
    }

    # Mocking sc and lr models
    app_module.model_cache['sc'] = MagicMock()
    app_module.model_cache['sc'].transform.return_value = [[1, 2, 3]]

    app_module.model_cache['lr'] = MagicMock()
    app_module.model_cache['lr'].predict.return_value = [42.0]

    rv = client.post('/predict', data=data)
    assert rv.status_code == 200
    assert b'mocked_result' in rv.data
