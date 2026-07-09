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
        # 🛡️ Sentinel: Validate input and handle type casting errors to prevent 500 errors and stack trace exposure
        item_weight= float(request.form['item_weight'])
        item_fat_content=float(request.form['item_fat_content'])
        item_visibility= float(request.form['item_visibility'])
        item_type= float(request.form['item_type'])
        item_mrp = float(request.form['item_mrp'])
        outlet_establishment_year= float(request.form['outlet_establishment_year'])
        outlet_size= float(request.form['outlet_size'])
        outlet_location_type= float(request.form['outlet_location_type'])
        outlet_type= float(request.form['outlet_type'])
    except (ValueError, KeyError):
        return "Bad Request", 400

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    scaler_path=r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\sc.sav"

    sc=joblib.load(scaler_path)

    X_std= sc.transform(X)

    model_path=r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\lr.sav"

    model= joblib.load(model_path)

    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    # 🛡️ Sentinel: Disable debug mode in production to prevent Werkzeug interactive debugger and stack trace exposure
    app.run(debug=False, port=9457)
