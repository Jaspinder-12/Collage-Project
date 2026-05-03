import pytest
import sys
from unittest.mock import MagicMock

# Mock joblib and its functions before importing app
sys.modules["joblib"] = MagicMock()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client, mocker):
    # Mock render_template to avoid Jinja template missing errors
    mocker.patch("app.render_template", return_value="Mocked Home")
    rv = client.get("/")
    assert rv.status_code == 200
