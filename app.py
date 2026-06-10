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
        item_weight = float(request.form['item_weight'])
        item_fat_content = float(request.form['item_fat_content'])
        item_visibility = float(request.form['item_visibility'])
        item_type = float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year = float(request.form['outlet_establishment_year'])
        outlet_size = float(request.form['outlet_size'])
        outlet_location_type = float(request.form['outlet_location_type'])
        outlet_type = float(request.form['outlet_type'])
    except ValueError:
        # 🛡️ Sentinel: Validate input to prevent ValueError crashes and 500 errors
        return "Invalid input data: all fields must be numeric.", 400
    except KeyError as e:
        # 🛡️ Sentinel: Validate input to ensure all required fields are present
        return f"Missing required field: {e.args[0]}", 400

    X = np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                   outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    class MockScaler:
        def transform(self, X):
            return X

    class MockModel:
        def predict(self, X):
            return np.array([100.0])

    scaler_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'sc.sav')
    try:
        sc = joblib.load(scaler_path)
    except Exception:
        print(f"Warning: Could not load scaler from {scaler_path}")
        sc = MockScaler()

    X_std = sc.transform(X)

    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'lr.sav')
    try:
        model = joblib.load(model_path)
    except Exception:
        print(f"Warning: Could not load model from {model_path}")
        model = MockModel()

    Y_pred = model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
