import pytest
import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

def test_app_import():
    """Test that the app can be imported successfully."""
    assert app is not None
