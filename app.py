from flask import Flask, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Load models at startup
model_dir = os.path.join(os.path.dirname(__file__), 'models')
scaler_path = os.path.join(model_dir, 'sc.sav')
model_path = os.path.join(model_dir, 'lr.sav')

try:
    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
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
        outlet_establishment_year = float(request.form['outlet_establishment_year'])
        outlet_size = float(request.form['outlet_size'])
        outlet_location_type = float(request.form['outlet_location_type'])
        outlet_type = float(request.form['outlet_type'])

        X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                       outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

        if sc is None or model is None:
            return "Models not loaded", 500

        X_std = sc.transform(X)
        Y_pred = model.predict(X_std)

        # Handle prediction output format
        prediction = float(Y_pred[0]) if isinstance(Y_pred, (list, np.ndarray)) else float(Y_pred)

        return render_template("result.html", prediction=prediction)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=9457)
