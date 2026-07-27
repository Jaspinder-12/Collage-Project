import pytest
import sys


class MockModel:
    def predict(self, x):
        return [0]

    def transform(self, x):
        return x


sys.modules["joblib"] = type("MockJoblib", (), {"load": lambda p: MockModel()})
import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    pass
