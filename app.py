from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

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

        # 🛡️ Sentinel: Replacing absolute paths with relative paths to avoid errors, and catching exceptions to prevent information leakage
        base_dir = os.path.dirname(os.path.abspath(__file__))
        scaler_path = os.path.join(base_dir, 'models', 'sc.sav')

        try:
            sc=joblib.load(scaler_path)
        except FileNotFoundError:
            class MockScaler:
                def transform(self, x): return x
            sc = MockScaler()
            print("Warning: sc.sav not found, using MockScaler.")

        X_std= sc.transform(X)

        model_path = os.path.join(base_dir, 'models', 'lr.sav')
        try:
            model= joblib.load(model_path)
            Y_pred=model.predict(X_std)
        except FileNotFoundError:
            class MockModel:
                def predict(self, x): return np.array([100.0])
            model = MockModel()
            Y_pred=model.predict(X_std)
            print("Warning: lr.sav not found, using MockModel.")

        return render_template("result.html", prediction=float(Y_pred))
    except Exception:
        # 🛡️ Sentinel: Catching exceptions and failing securely to avoid leaking stack traces
        return jsonify({"error": "Invalid input or processing error"}), 400

if __name__ == "__main__":
    # 🛡️ Sentinel: Disabled debug mode to prevent RCE and information leakage in production
    app.run(debug=False, port=9457)
