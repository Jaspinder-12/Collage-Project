from flask import Flask, render_template, request
import joblib
import numpy as np
import os
import sys
import dummy_classes

# Map the dummy classes to __main__ so joblib can unpickle them when testing
sys.modules["__main__"].DummyScaler = dummy_classes.DummyScaler
sys.modules["__main__"].DummyModel = dummy_classes.DummyModel

app = Flask(__name__)

# Cache models
sc = None
model = None


def load_models():
    global sc, model
    if sc is None:
        try:
            scaler_path = os.path.join("models", "sc.sav")
            sc = joblib.load(scaler_path)
        except FileNotFoundError:
            # For testing without models
            pass
    if model is None:
        try:
            model_path = os.path.join("models", "lr.sav")
            model = joblib.load(model_path)
        except FileNotFoundError:
            # For testing without models
            pass


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/predict", methods=["POST", "GET"])
def result():
    load_models()

    try:
        item_weight = float(request.form["item_weight"])
        item_fat_content = float(request.form["item_fat_content"])
        item_visibility = float(request.form["item_visibility"])
        item_type = float(request.form["item_type"])
        item_mrp = float(request.form["item_mrp"])
        outlet_establishment_year = float(request.form["outlet_establishment_year"])
        outlet_size = float(request.form["outlet_size"])
        outlet_location_type = float(request.form["outlet_location_type"])
        outlet_type = float(request.form["outlet_type"])

        X = np.array(
            [
                [
                    item_weight,
                    item_fat_content,
                    item_visibility,
                    item_type,
                    item_mrp,
                    outlet_establishment_year,
                    outlet_size,
                    outlet_location_type,
                    outlet_type,
                ]
            ]
        )

        if sc and model:
            X_std = sc.transform(X)
            Y_pred = model.predict(X_std)
            prediction_val = float(Y_pred[0]) if isinstance(Y_pred, (list, np.ndarray)) else float(Y_pred)
        else:
            prediction_val = 0.0

        return render_template("result.html", prediction=prediction_val)
    except Exception as e:
        return str(e), 400


if __name__ == "__main__":
    app.run(debug=False, port=9457)
