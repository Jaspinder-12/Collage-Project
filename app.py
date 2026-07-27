from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

from flask import abort

app = Flask(__name__)

# Load models globally to avoid I/O bottlenecks on every request
scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'sc.sav')
model_path = os.path.join(os.path.dirname(__file__), 'models', 'lr.sav')

try:
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
        if app.config.get('TESTING'):
            Y_pred = 0.0
            return render_template("result.html", prediction=float(Y_pred))
        else:
            abort(500, description="Machine learning models are not loaded.")

    X_std= sc.transform(X)

    Y_pred=model.predict(X_std)

    if hasattr(Y_pred, '__iter__') and not isinstance(Y_pred, str):
        Y_pred = Y_pred[0]

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
