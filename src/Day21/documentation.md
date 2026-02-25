# Complete Machine Learning Workflow for House Price Prediction

## ✅ 1. Data Loading & Exploration

- Loaded house_price.csv with 4,600 rows and 18 columns
- Displayed dataset overview, data types, and statistics

## ✅ 2. Data Preparation

- Correctly dropped the target column (price) to create X (12 numeric features)
- Isolated the target column to create y (price values)
- Selected only numeric columns and removed missing values

## ✅ 3. Train-Test Split

- Split data: 80% training (3,680 samples), 20% testing (920 samples)
- Maintained proper data separation for unbiased evaluation

## ✅ 4. Feature Scaling

- Applied StandardScaler to normalize all features to the same scale
- Ensures consistent model training

## ✅ 5. Model Training

- Trained Linear Regression model on the scaled data
- Top predictive features: sqft_living, sqft_above, sqft_basement

## ✅ 6. Prediction & Evaluation

- Made predictions on both training and test sets
- Calculated performance metrics (MSE, RMSE, R² Score)
- Generated 10 sample predictions showing actual vs predicted prices
