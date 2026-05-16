from unittest.mock import patch, MagicMock
import app  # noqa: E402, F401
import numpy as np
import subprocess
import time
import urllib.request
import urllib.error
import pytest


@patch("app.render_template")
@patch("app.joblib.load")
def test_predict_route_caches_model(mock_joblib_load, mock_render_template):
    app.app.testing = True
    client = app.app.test_client()

    mock_scaler = MagicMock()
    mock_scaler.transform.return_value = np.array([[1]])
    mock_model = MagicMock()
    mock_model.predict.return_value = np.array([500.0])

    def side_effect(path):
        if "sc.sav" in path:
            return mock_scaler
        if "lr.sav" in path:
            return mock_model

    mock_joblib_load.side_effect = side_effect

    # First request
    client.post(
        "/predict",
        data={
            "item_weight": "1",
            "item_fat_content": "1",
            "item_visibility": "1",
            "item_type": "1",
            "item_mrp": "1",
            "outlet_establishment_year": "2000",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        },
    )

    assert mock_joblib_load.call_count == 2
    mock_render_template.assert_called_with("result.html", prediction=500.0)

    # Second request
    client.post(
        "/predict",
        data={
            "item_weight": "1",
            "item_fat_content": "1",
            "item_visibility": "1",
            "item_type": "1",
            "item_mrp": "1",
            "outlet_establishment_year": "2000",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        },
    )

    # joblib.load should NOT be called again
    assert mock_joblib_load.call_count == 2


def test_server_startup():
    process = subprocess.Popen(["python", "app.py"])
    time.sleep(2)  # Give the server time to start
    try:
        urllib.request.urlopen("http://127.0.0.1:9457")
    except urllib.error.HTTPError:
        pass  # Server is up but might return 500/404 due to missing templates
    except Exception as ex:
        pytest.fail(f"Server did not start: {ex}")
    finally:
        process.terminate()
        process.wait()
