import pytest
from unittest.mock import patch


class DummyModel:
    def transform(self, X):
        return X

    def predict(self, X):
        return 42.0


@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    import joblib

    def mock_load(filepath):
        return DummyModel()

    monkeypatch.setattr(joblib, "load", mock_load)


@pytest.fixture
def app():
    import app as myapp

    # Reset cache to isolate tests
    myapp.model_cache = {}
    myapp.app.config.update(
        {
            "TESTING": True,
        }
    )
    yield myapp.app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index(client):
    with patch("app.render_template") as mock_render:
        mock_render.return_value = "Mocked template"
        response = client.get("/")
        assert response.status_code == 200
        mock_render.assert_called_once_with("home.html")


def test_predict(client):
    with patch("app.render_template") as mock_render:
        mock_render.return_value = "Mocked template"
        response = client.post(
            "/predict",
            data={
                "item_weight": "12.5",
                "item_fat_content": "0",
                "item_visibility": "0.05",
                "item_type": "1",
                "item_mrp": "150.0",
                "outlet_establishment_year": "1999",
                "outlet_size": "1",
                "outlet_location_type": "0",
                "outlet_type": "1",
            },
        )
        assert response.status_code == 200
        mock_render.assert_called_once_with("result.html", prediction=42.0)


def test_predict_lazy_loading(client):
    import app as myapp

    with patch("app.render_template") as mock_render:
        mock_render.return_value = "Mocked template"

        # Cache is initially empty
        assert "sc" not in myapp.model_cache
        assert "lr" not in myapp.model_cache

        client.post(
            "/predict",
            data={
                "item_weight": "12.5",
                "item_fat_content": "0",
                "item_visibility": "0.05",
                "item_type": "1",
                "item_mrp": "150.0",
                "outlet_establishment_year": "1999",
                "outlet_size": "1",
                "outlet_location_type": "0",
                "outlet_type": "1",
            },
        )

        # Cache is populated after first request
        assert "sc" in myapp.model_cache
        assert "lr" in myapp.model_cache
