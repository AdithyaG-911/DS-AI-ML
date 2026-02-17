# Demonstrating Why We Choose StandardScaler vs MinMaxScaler

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# -------------------- Create Sample Dataset --------------------
np.random.seed(0)
df = pd.DataFrame({
    "Age": np.random.randint(20, 60, 100),
    "Salary": np.random.randint(20000, 120000, 100)
})

# Dummy target variable (for demonstration)
y = np.random.randint(0, 2, 100)

# -------------------- Standard Scaling --------------------
standard_scaler = StandardScaler()
X_standard = standard_scaler.fit_transform(df)

# -------------------- Min-Max Scaling --------------------
minmax_scaler = MinMaxScaler()
X_minmax = minmax_scaler.fit_transform(df)

# -------------------- Apply Algorithms --------------------
knn = KNeighborsClassifier(n_neighbors=3)
svm = SVC()

knn.fit(X_standard, y)
svm.fit(X_standard, y)

# -------------------- Explanation Print Statements --------------------
print("SCALING COMPARISON SUMMARY\n")

print("1. StandardScaler Applied:")
print("   - Data mean is centered at 0")
print("   - Standard deviation becomes 1")
print("   - Best suited for algorithms assuming normally distributed data")
print("   - Used here for SVM because SVM works better when features are centered\n")

print("2. MinMaxScaler Applied:")
print("   - Data scaled between 0 and 1")
print("   - Preserves shape of original distribution")
print("   - Commonly used in Neural Networks and KNN\n")

print("WHY SCALING IS IMPORTANT:")
print("   - Without scaling, Salary (20000–120000) dominates Age (20–60)")
print("   - Distance-based algorithms (KNN, SVM) rely on Euclidean distance")
print("   - Scaling ensures both features contribute equally\n")

print("Model training completed successfully with scaled data.")
