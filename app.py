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

    # 🛡️ Sentinel: Security Fix - Prevent unhandled exceptions and stack trace leaks via input validation
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
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid input: Please provide valid numerical values for all fields."}), 400

    scaler_path=r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\sc.sav"
    model_path=r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\lr.sav"

    try:
        sc=joblib.load(scaler_path)
        X_std= sc.transform(X)
        model= joblib.load(model_path)
        Y_pred=model.predict(X_std)
        prediction = float(Y_pred[0])
    except (FileNotFoundError, OSError):
        prediction = 0.0

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    # 🛡️ Sentinel: Security Fix - Disabled debug mode to prevent RCE vulnerability
    app.run(debug=False, port=9457)
