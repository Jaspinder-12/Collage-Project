from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

# ⚡ Bolt: Globally cache models in memory to avoid severe performance degradation from repetitive disk I/O and deserialization
# ⚡ Bolt: Use relative paths so the application can load models regardless of the environment (e.g. CI)
base_dir = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(base_dir, "models", "sc.sav")
model_path = os.path.join(base_dir, "models", "lr.sav")

# Let exceptions propagate to fail loudly if critical ML models are missing
sc = joblib.load(scaler_path)
model = joblib.load(model_path)


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

    X_std = sc.transform(X)
    Y_pred = model.predict(X_std)
    # ⚡ Bolt: Explicitly index the first element of the prediction array to prevent DeprecationWarnings
    prediction = float(Y_pred[0])

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=False, port=9457)
