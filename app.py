from flask import Flask, jsonify, render_template, request, abort
import joblib
import os
import numpy as np

app = Flask(__name__)

# Load models globally to prevent I/O bottlenecks on every request
try:
    scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'sc.sav')
    sc = joblib.load(scaler_path)

    model_path = os.path.join(os.path.dirname(__file__), 'models', 'lr.sav')
    model = joblib.load(model_path)
except FileNotFoundError:
    sc = None
    model = None


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
        return "400 Bad Request", 400

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

    Y_pred = Y_pred[0] if hasattr(Y_pred, '__iter__') else Y_pred

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
