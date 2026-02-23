from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def result():
    try:
        # Input validation: check for missing or invalid values
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

        # Security Fix: Use relative paths instead of hardcoded absolute paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(base_dir, 'models')

        scaler_path = os.path.join(models_dir, 'sc.sav')
        sc=joblib.load(scaler_path)

        X_std= sc.transform(X)

        model_path = os.path.join(models_dir, 'lr.sav')
        model= joblib.load(model_path)

        Y_pred=model.predict(X_std)

        # Handle prediction result safely
        prediction_value = float(Y_pred[0]) if hasattr(Y_pred, '__getitem__') and len(Y_pred) > 0 else float(Y_pred)

        return render_template("result.html", prediction=prediction_value)

    except ValueError:
        return "Invalid input: Please ensure all fields contain valid numbers.", 400
    except KeyError:
        return "Missing input: Please fill in all fields.", 400
    except Exception:
        # Log the error securely (not implemented here) but return a generic message
        return "An internal error occurred.", 500

if __name__ == "__main__":
    # Security Fix: Disable debug mode in production
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=9457)
