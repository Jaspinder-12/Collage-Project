from flask import Flask, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

model_cache = {}


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/predict", methods=["POST", "GET"])
def result():

    item_weight = float(request.form["item_weight"])
    item_fat_content = float(request.form["item_fat_content"])
    item_visibility = float(request.form["item_visibility"])
    item_type = float(request.form["item_type"])
    item_mrp = float(request.form["item_mrp"])
    outlet_est_year = float(request.form["outlet_establishment_year"])
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
                outlet_est_year,
                outlet_size,
                outlet_location_type,
                outlet_type,
            ]
        ]
    )

    # ⚡ Bolt: Performance optimization - Lazy-load and cache models
    # to prevent I/O blocking per request
    if "sc" not in model_cache or "lr" not in model_cache:
        base_dir = os.path.dirname(__file__)
        scaler_path = os.path.join(base_dir, "models", "sc.sav")
        model_cache["sc"] = joblib.load(scaler_path)

        model_path = os.path.join(base_dir, "models", "lr.sav")
        model_cache["lr"] = joblib.load(model_path)

    sc = model_cache["sc"]
    model = model_cache["lr"]

    X_std = sc.transform(X)

    Y_pred = model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))


if __name__ == "__main__":
    app.run(debug=True, port=9457)
