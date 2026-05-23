from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

# ⚡ Bolt: Cache models globally to avoid repetitive disk I/O and deserialization during requests.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(BASE_DIR, 'models', 'sc.sav')
model_path = os.path.join(BASE_DIR, 'models', 'lr.sav')

sc = joblib.load(scaler_path)
model = joblib.load(model_path)


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
        return "Bad Request: Invalid input data", 400

    X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])

    X_std= sc.transform(X)
    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred[0]))

if __name__ == "__main__":
    app.run(debug=False, port=9457)
