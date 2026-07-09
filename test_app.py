import sys
from unittest.mock import MagicMock

sys.modules['joblib'] = MagicMock()

from app import app  # noqa: E402


def test_dummy():
    assert app
    assert True
