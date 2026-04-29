import sys
import pytest


class MockScaler:
    def transform(self, X):
        return X


class MockModel:
    def predict(self, X):
        return [100.5]


class MockJoblib:
    @staticmethod
    def load(path):
        if "sc.sav" in path:
            return MockScaler()
        return MockModel()


sys.modules["joblib"] = MockJoblib()

import app  # noqa: E402


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get("/")
    assert b"Home" in rv.data


def test_predict(client):
    rv = client.post(
        "/predict",
        data={
            "item_weight": "1",
            "item_fat_content": "2",
            "item_visibility": "3",
            "item_type": "4",
            "item_mrp": "5",
            "outlet_establishment_year": "6",
            "outlet_size": "7",
            "outlet_location_type": "8",
            "outlet_type": "9",
        },
    )
    assert b"Result" in rv.data
