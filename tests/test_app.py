import pytest
import sys
import os

# Ensure the app module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client, monkeypatch):
    """Test the index route (/) returns a 200 OK or handled properly when templates are missing."""
    # Since templates might be missing, we mock render_template
    monkeypatch.setattr('app.render_template', lambda template_name, **kwargs: f"Mocked {template_name}")
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mocked home.html" in response.data
