import numpy as np


def test_predict_caches_model(mocker):
    mock_load = mocker.patch("app.joblib.load")
    mock_sc = mocker.MagicMock()
    mock_model = mocker.MagicMock()

    def side_effect(path):
        if "sc.sav" in path:
            return mock_sc
        elif "lr.sav" in path:
            return mock_model

    mock_load.side_effect = side_effect

    mock_sc.transform.return_value = np.array([[0] * 9])
    mock_model.predict.return_value = np.array([42.0])

    mocker.patch("app.render_template", return_value="mocked")

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
