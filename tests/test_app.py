import pytest
import app

def test_index_route():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
