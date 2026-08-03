from flask import Flask, render_template, request
import joblib
import os
import numpy as np

# ⚡ Bolt: Cache machine learning models globally in memory at startup rather than
# synchronously loading from disk on each /predict request.
# This prevents disk I/O and deserialization from degrading response latency.
scaler_path = os.path.join('models', 'sc.sav')
sc = joblib.load(scaler_path)
model_path = os.path.join('models', 'lr.sav')
model = joblib.load(model_path)

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
    except (ValueError, KeyError):
        # 🛡️ Sentinel: Handle missing or invalid input to prevent 500 errors and stack trace leakage
        return render_template("home.html")

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    X_std= sc.transform(X)

    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    # 🛡️ Sentinel: Disable debug mode to prevent RCE and stack trace leakage in production
    app.run(debug=False, port=9457)
