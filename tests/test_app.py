import pytest
import app as app_module

@pytest.fixture
def client(monkeypatch):
    app_module.app.config['TESTING'] = True

    # Mock render_template
    def mock_render_template(template_name, **context):
        return f"Mock rendered {template_name} with {context}"
    monkeypatch.setattr(app_module, 'render_template', mock_render_template)

    with app_module.app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b'Mock rendered home.html' in rv.data

def test_predict_bad_request(client):
    # Missing parameters should return 400
    rv = client.post('/predict', data={})
    assert rv.status_code == 400
    assert b'Bad Request' in rv.data
