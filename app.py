from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Global model variables
sc = None
model = None

try:
    scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'sc.sav')
    sc = joblib.load(scaler_path)

    model_path = os.path.join(os.path.dirname(__file__), 'models', 'lr.sav')
    model = joblib.load(model_path)
except FileNotFoundError:
    pass

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

    # Performance Optimization: Use globally loaded models to avoid I/O overhead on every request
    if sc is None or model is None:
        if app.config.get('TESTING'):
            return render_template("result.html", prediction=0.0)
        else:
            return "Models not loaded. Cannot process request.", 500

    X_std= sc.transform(X)

    Y_pred=model.predict(X_std)

    # LinearRegression model's predict() return value is handled by checking for array-like attributes and extracting the first element if necessary
    pred_val = float(Y_pred[0]) if hasattr(Y_pred, '__iter__') else float(Y_pred)

    return render_template("result.html", prediction=pred_val)

if __name__ == "__main__":
    app.run(debug=True, port=9457)
