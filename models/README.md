# Models Directory

This directory should contain the trained machine learning models:
- `sc.sav`: The standard scaler.
- `lr.sav`: The linear regression model.

## How to Generate Models

The model files are not included in the repository to keep it lightweight.
To generate them, you need to run the training script or extract the model training code from `BigMart Sales Prediction - Updated.ipynb`.

The models should be compatible with the following schema:
- 9 features: `item_weight`, `item_fat_content`, `item_visibility`, `item_type`, `item_mrp`, `outlet_establishment_year`, `outlet_size`, `outlet_location_type`, `outlet_type`.
- `sc.sav` is a `StandardScaler`.
- `lr.sav` is a `LinearRegression`.
