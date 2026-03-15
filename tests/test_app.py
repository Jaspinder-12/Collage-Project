import pytest
from app import app as app_module

@pytest.fixture
def client():
    app_module.config['TESTING'] = True
    with app_module.test_client() as client:
        yield client

import app as app_file

def test_index(client, monkeypatch):
    monkeypatch.setattr(app_file, 'render_template', lambda template_name_or_list, **context: "mocked_home")
    rv = client.get('/')
    assert b'mocked_home' in rv.data

def test_predict(client, monkeypatch):
    monkeypatch.setattr(app_file, 'render_template', lambda template_name_or_list, **context: "mocked_result")
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
    rv = client.post('/predict', data=data)
    assert rv.status_code == 200
    assert b'mocked_result' in rv.data
