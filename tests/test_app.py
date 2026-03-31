import pytest

@pytest.fixture(autouse=True)
def mock_joblib_load(monkeypatch):
    class DummyScaler:
        def transform(self, x):
            return x

    class DummyModel:
        def predict(self, x):
            return 42.0

    def mock_load(filepath):
        if 'sc.sav' in filepath:
            return DummyScaler()
        elif 'lr.sav' in filepath:
            return DummyModel()
        return None

    import joblib
    monkeypatch.setattr(joblib, "load", mock_load)


@pytest.fixture
def client():
    import app
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_index_route(client, monkeypatch):
    import app

    # Mock render_template to return a dummy string without rendering the actual template
    def mock_render_template(template_name, **context):
        if template_name == "home.html":
            return "dummy_home_html"
        return "dummy_result_html"

    monkeypatch.setattr(app, 'render_template', mock_render_template)

    response = client.get("/")
    assert response.status_code == 200
    assert b"dummy_home_html" in response.data

def test_predict_route_invalid_input(client):
    response = client.post("/predict", data={})
    assert response.status_code == 400
    assert b"Invalid input. Please provide valid numeric values." in response.data
