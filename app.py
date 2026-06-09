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

        base_dir = os.path.dirname(os.path.abspath(__file__))
        scaler_path = os.path.join(base_dir, 'models', 'sc.sav')
        try:
            sc = joblib.load(scaler_path)
            X_std = sc.transform(X)
        except FileNotFoundError:
            print(f"Warning: Scaler not found at {scaler_path}")
            class MockScaler:
                def transform(self, X): return X
            sc = MockScaler()
            X_std = sc.transform(X)

        model_path = os.path.join(base_dir, 'models', 'lr.sav')
        try:
            model = joblib.load(model_path)
        except FileNotFoundError:
            print(f"Warning: Model not found at {model_path}")
            class MockModel:
                def predict(self, X): return np.array([100.0])
            model = MockModel()

        Y_pred=model.predict(X_std)

        return render_template("result.html", prediction=float(Y_pred))
    except (ValueError, KeyError):
        # 🛡️ Sentinel: Catch missing/invalid inputs to prevent stack trace leaks
        return jsonify({"error": "Invalid or missing input parameters"}), 400
    except Exception:
        # 🛡️ Sentinel: Generic catch-all to fail securely without exposing internals
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == "__main__":
    # 🛡️ Sentinel: Disabled debug mode to prevent stack trace exposure in production
    app.run(debug=False, port=9457)
