import numpy as np
from unittest.mock import patch, MagicMock


def test_predict_caches_model():
    with patch("app.joblib.load") as mock_load, patch(
        "app.render_template", return_value="mocked"
    ):

        mock_sc = MagicMock()
        mock_model = MagicMock()

        def side_effect(path):
            if "sc.sav" in path:
                return mock_sc
            elif "lr.sav" in path:
                return mock_model

        mock_load.side_effect = side_effect

        mock_sc.transform.return_value = np.array([[0] * 9])
        mock_model.predict.return_value = np.array([42.0])

        import app  # noqa: E402, F401

        app.model_cache.clear()

        client = app.app.test_client()
        data = {
            "item_weight": "1",
            "item_fat_content": "1",
            "item_visibility": "1",
            "item_type": "1",
            "item_mrp": "1",
            "outlet_establishment_year": "1",
            "outlet_size": "1",
            "outlet_location_type": "1",
            "outlet_type": "1",
        }

        res1 = client.post("/predict", data=data)
        assert res1.status_code == 200
        assert mock_load.call_count == 2

        res2 = client.post("/predict", data=data)
        assert res2.status_code == 200
        assert mock_load.call_count == 2
