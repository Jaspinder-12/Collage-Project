from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

# ⚡ Bolt: Cache machine learning models globally in memory at startup rather than
# synchronously loading from disk on each /predict request.
# This prevents disk I/O and deserialization from degrading response latency.
base_dir = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(base_dir, 'models', 'sc.sav')
sc = joblib.load(scaler_path)
model_path = os.path.join(base_dir, 'models', 'lr.sav')
model = joblib.load(model_path)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def result():
    try:
        item_weight= float(request.form['item_weight'])
        item_fat_content=float(request.form['item_fat_content'])
        item_visibility= float(request.form['item_visibility'])
        item_type= float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year= float(request.form['outlet_establishment_year'])
        outlet_size= float(request.form['outlet_size'])
        outlet_location_type= float(request.form['outlet_location_type'])
        outlet_type= float(request.form['outlet_type'])

        X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                      outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

        X_std= sc.transform(X)
        Y_pred=model.predict(X_std)
        # 🛡️ Sentinel: Safe error handling without leaking stack traces. Added try/except to prevent 500 errors on invalid input.

        return render_template("result.html", prediction=float(Y_pred))
    except (ValueError, KeyError):
        return render_template("home.html", error="Invalid input. Please provide valid numbers for all fields.")

if __name__ == "__main__":
    # 🛡️ Sentinel: Disable debug mode to prevent RCE and stack trace leakage in production
    app.run(debug=False, port=9457)
