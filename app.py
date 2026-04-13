from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# ⚡ Bolt: Performance optimization - lazy load ML models
model_cache = {}

def get_model(model_name):
    if model_name not in model_cache:
        model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_name}.sav')
        model_cache[model_name] = joblib.load(model_path)
    return model_cache[model_name]


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

    sc = get_model('sc')
    X_std= sc.transform(X)

    model = get_model('lr')
    Y_pred=model.predict(X_std)

    return render_template("result.html", prediction=float(Y_pred[0] if isinstance(Y_pred, (list, np.ndarray)) else Y_pred))

if __name__ == "__main__":
    app.run(port=9457)
