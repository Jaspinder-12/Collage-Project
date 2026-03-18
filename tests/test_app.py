import pytest
import app as app_module


@pytest.fixture
def client(monkeypatch):
    # Mock render_template since we don't have template files in the repo
    monkeypatch.setattr(
        app_module,
        'render_template',
        lambda template_name, **kwargs: template_name
    )
    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client


def test_index_route(client):
    """Test the root route returns the correct template."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "home.html"


def test_predict_route_missing_model(client):
    """Test the predict route when models are missing (in testing mode)."""
    # Create valid payload
    data = {
        'item_weight': '10.5',
        'item_fat_content': '1',
        'item_visibility': '0.05',
        'item_type': '1',
        'item_mrp': '150.0',
        'outlet_establishment_year': '1999',
        'outlet_size': '1',
        'outlet_location_type': '1',
        'outlet_type': '1'
    }
    response = client.post("/predict", data=data)
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "result.html"
