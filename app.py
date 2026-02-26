import os
import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load models globally to avoid reloading on every request
# (Performance Optimization)
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')
SCALER_PATH = os.path.join(MODEL_DIR, 'sc.sav')
MODEL_PATH = os.path.join(MODEL_DIR, 'lr.sav')

try:
    sc = joblib.load(SCALER_PATH)
    model = joblib.load(MODEL_PATH)
    print("Models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")
    sc = None
    model = None


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
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
            item_weight,
            item_fat_content,
            item_visibility,
            item_type,
            item_mrp,
            outlet_establishment_year,
            outlet_size,
            outlet_location_type,
            outlet_type
        ]])

        if sc and model:
            X_std = sc.transform(X)
            Y_pred = model.predict(X_std)
            # Y_pred is an array, we need the scalar value
            return render_template("result.html", prediction=float(Y_pred[0]))
        else:
            return "Models not loaded correctly", 500

    # For GET request on /predict, just render home or redirect
    return render_template("home.html")


if __name__ == "__main__":
    # Security: Don't use debug=True in production
    app.run(debug=True, port=9457)
