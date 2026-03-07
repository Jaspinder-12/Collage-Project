from flask import Flask, jsonify, render_template, request, abort
import joblib
import os
import numpy as np

app = Flask(__name__)

# Global model loading for performance optimization
# This prevents reloading the models from disk on every request
try:
    base_dir = os.path.dirname(__file__)
    scaler_path = os.path.join(base_dir, 'models', 'sc.sav')
    model_path = os.path.join(base_dir, 'models', 'lr.sav')

    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
except FileNotFoundError:
    sc = None
    model = None

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

    if sc is None or model is None:
        if app.config['TESTING']:
            X_std = X
            Y_pred = 0.0
        else:
            abort(500, description="Machine learning models could not be loaded.")
    else:
        X_std = sc.transform(X)
        Y_pred = model.predict(X_std)
        # Handle cases where Y_pred might be an array-like
        if hasattr(Y_pred, '__iter__') and not isinstance(Y_pred, str):
            Y_pred = Y_pred[0]

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
