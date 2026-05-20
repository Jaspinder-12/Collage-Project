from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# ⚡ Bolt: Cache models globally to prevent repeated disk I/O on every request
scaler_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\sc.sav"
model_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\lr.sav"
try:
    GLOBAL_SCALER = joblib.load(scaler_path)
    GLOBAL_MODEL = joblib.load(model_path)
except Exception:
    GLOBAL_SCALER = None
    GLOBAL_MODEL = None


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def result():

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

    # ⚡ Bolt: Use globally cached models if available, fallback to local load
    if GLOBAL_SCALER and GLOBAL_MODEL:
        sc = GLOBAL_SCALER
        model = GLOBAL_MODEL
    else:
        scaler_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\sc.sav"
        sc = joblib.load(scaler_path)
        model_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\lr.sav"
        model = joblib.load(model_path)

    X_std= sc.transform(X)

    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred[0]))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
