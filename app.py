from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

# Construct paths relative to the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCALER_PATH = os.path.join(BASE_DIR, 'models', 'sc.sav')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'lr.sav')


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        try:
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

            if not os.path.exists(SCALER_PATH) or not os.path.exists(MODEL_PATH):
                return "Error: Model files not found. Please follow instructions in models/README.md to generate them.", 500

            sc = joblib.load(SCALER_PATH)
            X_std = sc.transform(X)

            model = joblib.load(MODEL_PATH)
            Y_pred = model.predict(X_std)

            # Ensure we are passing a float
            # Depending on sklearn version and model, predict returns array
            prediction_value = float(Y_pred[0]) if hasattr(Y_pred, '__getitem__') and len(Y_pred) > 0 else float(Y_pred)

            return render_template("result.html", prediction="{:.2f}".format(prediction_value))

        except KeyError as e:
            return f"Missing form field: {e}", 400
        except ValueError as e:
            return f"Invalid input: {e}", 400
        except Exception as e:
            return f"An error occurred: {e}", 500

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=9457)
