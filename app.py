from flask import Flask, jsonify, render_template, request
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():

    try:
        # 🛡️ Sentinel: Security Fix - Prevent 500 error and stack trace leakage by safely handling input
        item_weight = float(request.form['item_weight'])
        item_fat_content = float(request.form['item_fat_content'])
        item_visibility = float(request.form['item_visibility'])
        item_type = float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year = float(
            request.form['outlet_establishment_year'])
        outlet_size = float(request.form['outlet_size'])
        outlet_location_type = float(request.form['outlet_location_type'])
        outlet_type = float(request.form['outlet_type'])

        X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                      outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])
    except (ValueError, KeyError):
        # 🛡️ Sentinel: Security Fix - Return safe 400 response for invalid input
        return jsonify({"error": "Invalid input provided"}), 400

    scaler_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\sc.sav"

    sc = joblib.load(scaler_path)

    X_std = sc.transform(X)

    model_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\lr.sav"

    model = joblib.load(model_path)

    Y_pred = model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))


if __name__ == "__main__":
    # 🛡️ Sentinel: Security Fix - Disable Werkzeug debugger to prevent RCE
    app.run(debug=False, port=9457)
