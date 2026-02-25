from flask import Flask, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Performance Optimization: Load models once at startup
# This prevents reloading the model from disk on every request,
# significantly reducing latency.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')

scaler_path = os.path.join(MODEL_DIR, 'sc.sav')
model_path = os.path.join(MODEL_DIR, 'lr.sav')

# Load models globally
sc = joblib.load(scaler_path)
model = joblib.load(model_path)


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
    outlet_establishment_year = float(
        request.form['outlet_establishment_year']
    )
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[
        item_weight, item_fat_content, item_visibility, item_type, item_mrp,
        outlet_establishment_year, outlet_size, outlet_location_type,
        outlet_type
    ]])

    X_std = sc.transform(X)

    Y_pred = model.predict(X_std)

    # Y_pred is a numpy array (e.g. [1234.5]), access the first element
    return render_template("result.html", prediction=float(Y_pred[0]))


if __name__ == "__main__":
    app.run(debug=True, port=9457)
