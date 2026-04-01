# Models Directory

This directory should contain the trained machine learning models:
- `sc.sav`: The standard scaler.
- `lr.sav`: The linear regression model.

## How to Generate Models

The model files are not included in the repository to keep it lightweight or were missing.
To generate them, you need to run the training script.

If you have the environment set up (with pandas, sklearn, joblib, etc.):

1.  Open `BigMart Sales Prediction - Updated.ipynb` in Jupyter Notebook.
2.  Run the cells up to the model saving part.
3.  Ensure the paths in `joblib.dump()` point to this `models/` directory.

Alternatively, you can extract the relevant Python code into a `train.py` script.
