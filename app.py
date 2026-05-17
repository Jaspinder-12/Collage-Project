from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# ⚡ Bolt: Performance Optimization - Cache ML assets to avoid disk I/O on every request
ml_cache = {}


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict', methods=['POST', 'GET'])
def result():

    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                   outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

    scaler_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\sc.sav"
    model_path = r"D:\projects\BigMart-Sales-Prediction-With-Deployment-main\models\lr.sav"

    if 'sc' not in ml_cache or 'model' not in ml_cache:
        ml_cache['sc'] = joblib.load(scaler_path)
        ml_cache['model'] = joblib.load(model_path)

    sc = ml_cache['sc']
    model = ml_cache['model']

    X_std = sc.transform(X)
    Y_pred = model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred[0]))


if __name__ == "__main__":
    app.run(debug=False, port=9457)
