from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# ⚡ Bolt: Cache ML models globally to prevent expensive synchronous disk I/O and deserialization on every request
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(BASE_DIR, "models", "sc.sav")
model_path = os.path.join(BASE_DIR, "models", "lr.sav")

# ⚡ Bolt: Allow FileNotFoundError to fail loudly if models are missing, ensuring state consistency on startup
sc = joblib.load(scaler_path)
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

    try:
        X = np.array([[float(item_weight), float(item_fat_content), float(item_visibility), float(item_type), float(item_mrp),
                      float(outlet_establishment_year), float(outlet_size), float(outlet_location_type), float(outlet_type)]])
    except ValueError:
        return render_template("home.html")

    X_std= sc.transform(X)

    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
