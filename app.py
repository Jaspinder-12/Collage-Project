from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

# Cache models in memory at startup
base_dir = os.path.dirname(os.path.abspath(__file__))
sc = joblib.load(os.path.join(base_dir, 'models', 'sc.sav'))
model = joblib.load(os.path.join(base_dir, 'models', 'lr.sav'))

@app.route('/predict',methods=['POST','GET'])
def result():
    try:
        # 🛡️ Sentinel: Validate input and handle missing or invalid data gracefully to prevent 500 errors and stack trace exposure
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

        X_std= sc.transform(X)
        Y_pred=model.predict(X_std)

        return render_template("result.html", prediction=float(Y_pred))
    except (ValueError, KeyError):
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=False, port=9457)
