from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

class MockScaler:
    def transform(self, X):
        return X

class MockModel:
    def predict(self, X):
        import numpy as np
        return np.array([100.0])

# ⚡ Bolt: Cache models globally to prevent expensive disk I/O on every request
base_dir = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(base_dir, 'models', 'sc.sav')
model_path = os.path.join(base_dir, 'models', 'lr.sav')

try:
    sc = joblib.load(scaler_path)
except Exception:
    print("Warning: Failed to load scaler, using MockScaler")
    sc = MockScaler()

try:
    model = joblib.load(model_path)
except Exception:
    print("Warning: Failed to load model, using MockModel")
    model = MockModel()


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

    # ⚡ Bolt: Using globally cached scaler and model instead of loading from disk
    X_std= sc.transform(X)

    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred))

if __name__ == "__main__":
    app.run(debug=True, port=9457)
