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
    except (KeyError, ValueError, TypeError):
        return "Bad Request: Invalid or missing form data.", 400

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    scaler_path=os.path.join(os.path.dirname(__file__), 'models', 'sc.sav')

    try:
        sc=joblib.load(scaler_path)
    except FileNotFoundError:
        sc = None

    if sc is not None:
        X_std= sc.transform(X)
    else:
        X_std = X

    model_path=os.path.join(os.path.dirname(__file__), 'models', 'lr.sav')

    try:
        model= joblib.load(model_path)
    except FileNotFoundError:
        model = None

    if model is not None:
        Y_pred=model.predict(X_std)
    else:
        Y_pred = 0.0 # Graceful fallback if model is not present

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=False, port=9457)
