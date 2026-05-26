from flask import Flask, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# ⚡ Bolt: Caching models globally to avoid repetitive disk I/O on every request
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(_BASE_DIR, 'models', 'sc.sav')
sc = joblib.load(SCALER_PATH)

MODEL_PATH = os.path.join(_BASE_DIR, 'models', 'lr.sav')
model = joblib.load(MODEL_PATH)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    _year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    _location = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[
        item_weight, item_fat_content, item_visibility, item_type,
        item_mrp, _year, outlet_size, _location, outlet_type
    ]])

    X_std = sc.transform(X)
    Y_pred = model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred[0]))


if __name__ == "__main__":
    app.run(debug=False, port=9457)
