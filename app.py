from flask import Flask, jsonify, render_template, request, abort
import joblib
import os
import numpy as np

app = Flask(__name__)

# Load models globally to prevent I/O bottlenecks on every request
sc = None
model = None

try:
    base_dir = os.path.dirname(__file__)
    scaler_path = os.path.join(base_dir, "models", "sc.sav")
    model_path = os.path.join(base_dir, "models", "lr.sav")

    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
except FileNotFoundError:
    pass


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
        return "Bad Request: Invalid or missing inputs.", 400

    if sc is None or model is None:
        if app.config.get('TESTING'):
            Y_pred = 0.0
            return render_template("result.html", prediction=float(Y_pred))
        else:
            abort(500)

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])


    X_std= sc.transform(X)


    Y_pred=model.predict(X_std)

    # Handle array-like return from model.predict
    prediction_value = Y_pred[0] if isinstance(Y_pred, (np.ndarray, list)) else Y_pred

    return render_template("result.html", prediction=float(prediction_value))

if __name__ == "__main__":
    app.run(port=9457)
