import pytest
import app as main_app

@pytest.fixture
def app():
    main_app.app.config.update({"TESTING": True})
    yield main_app.app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client, monkeypatch):
    monkeypatch.setattr(main_app, 'render_template', lambda template_name, **kwargs: "Mocked Template")
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Mocked Template"
