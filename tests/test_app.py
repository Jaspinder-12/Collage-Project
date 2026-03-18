import pytest
import app as app_module
from unittest.mock import MagicMock

@pytest.fixture
def client(monkeypatch):
    # Mock render_template to just return a string so we don't need templates
    monkeypatch.setattr(app_module, "render_template", lambda template_name, **context: "Mocked template")

    # Mock joblib.load to return a dummy scaler/model
    class DummyModel:
        def transform(self, X):
            return X
        def predict(self, X):
            return 0.0

    monkeypatch.setattr(app_module.joblib, "load", lambda path: DummyModel())

    app_module.app.config['TESTING'] = True
    with app_module.app.test_client() as client:
        yield client

def test_index(client):
    """Test that the index page loads."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mocked template" in response.data

def test_predict_invalid_data(client):
    """Test that invalid POST data to /predict returns 400."""
    response = client.post("/predict", data={
        "item_weight": "not a float",
        # missing other fields to trigger KeyError too
    })
    assert response.status_code == 400
    assert b"Invalid input data" in response.data

def test_predict_valid_data(client):
    """Test that valid POST data to /predict returns a prediction (0.0 in testing mode)."""
    response = client.post("/predict", data={
        "item_weight": "1.0",
        "item_fat_content": "1.0",
        "item_visibility": "1.0",
        "item_type": "1.0",
        "item_mrp": "1.0",
        "outlet_establishment_year": "2000",
        "outlet_size": "1.0",
        "outlet_location_type": "1.0",
        "outlet_type": "1.0"
    })
    assert response.status_code == 200
    assert b"Mocked template" in response.data
