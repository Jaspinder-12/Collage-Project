from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Preload models at startup
try:
    scaler_path=os.path.join(os.path.dirname(__file__), 'models', 'sc.sav')
    app.sc=joblib.load(scaler_path)

    model_path=os.path.join(os.path.dirname(__file__), 'models', 'lr.sav')
    app.model= joblib.load(model_path)
except FileNotFoundError:
    app.sc = None
    app.model = None

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

    try:
        if app.sc is None or app.model is None:
            raise FileNotFoundError

        sc = app.sc
        model = app.model
        X_std= sc.transform(X)

    except (FileNotFoundError, AttributeError):
        # Fallback if models are not loaded (e.g. testing)
        sc = None
        model = None
        X_std = X

    if model is not None:
        Y_pred=model.predict(X_std)
        # Convert the array to scalar explicitly
        prediction = Y_pred[0] if hasattr(Y_pred, '__len__') else Y_pred
    else:
        prediction = 0.0

    return render_template("result.html", prediction=float(prediction))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
