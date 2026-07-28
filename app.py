from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# ⚡ Bolt: Cache machine learning models in memory at startup to avoid synchronous disk I/O
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sc = joblib.load(os.path.join(BASE_DIR, 'models', 'sc.sav'))
model = joblib.load(os.path.join(BASE_DIR, 'models', 'lr.sav'))


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

        X= np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                      outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])
    except (ValueError, KeyError):
        return render_template("home.html")

    # ⚡ Bolt: Use globally cached scaler to avoid disk I/O overhead on every request
    X_std= sc.transform(X)

    # ⚡ Bolt: Use globally cached model to prevent deserialization latency during prediction
    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=False, port=9457)
