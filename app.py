from flask import Flask, render_template, request
import joblib
import os
import numpy as np


app = Flask(__name__)

# Cache models
sc = None
model = None


def get_models():
    global sc, model
    if sc is None:
        scaler_path = os.path.join(
            os.path.dirname(__file__), "models", "sc.sav")
        sc = joblib.load(scaler_path)
    if model is None:
        model_path = os.path.join(
            os.path.dirname(__file__), "models", "lr.sav")
        model = joblib.load(model_path)
    return sc, model


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    sc_local, model_local = get_models()

    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_est_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[
        item_weight, item_fat_content, item_visibility, item_type, item_mrp,
        outlet_est_year, outlet_size, outlet_location_type, outlet_type
    ]])

    # ⚡ Bolt: Use lazily loaded models to prevent redundant I/O operations
    X_std = sc_local.transform(X)
    Y_pred = model_local.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))


if __name__ == "__main__":
    app.run(debug=True, port=9457)
