import pytest
import app

def test_index_route(monkeypatch):
    app.app.config['TESTING'] = True

    # Mock render_template to prevent TemplateNotFound
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: 'mocked template')

    with app.app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
