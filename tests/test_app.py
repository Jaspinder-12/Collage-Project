import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client, monkeypatch):
    import app as app_module

    # Mock render_template to avoid TemplateNotFound since templates missing
    monkeypatch.setattr(
        app_module,
        "render_template",
        lambda t, **kwargs: b"home.html",
    )

    response = client.get("/")
    assert response.status_code == 200
    assert b"home.html" in response.data
