from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Load models once at startup to improve request latency
sc = None
model = None

def load_models():
    global sc, model
    if sc is None:
        scaler_path = os.path.join(os.path.dirname(__file__), 'models', 'sc.sav')
        sc = joblib.load(scaler_path)
    if model is None:
        model_path = os.path.join(os.path.dirname(__file__), 'models', 'lr.sav')
        model = joblib.load(model_path)


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

    load_models()

    X_std = sc.transform(X)

    # Predict and convert array to float for template
    Y_pred = model.predict(X_std)
    prediction_value = float(Y_pred[0]) if hasattr(Y_pred, '__len__') else float(Y_pred)

    return render_template("result.html", prediction=prediction_value)

if __name__ == "__main__":
    app.run(debug=True, port=9457)
