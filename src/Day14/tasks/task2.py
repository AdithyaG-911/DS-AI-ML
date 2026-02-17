import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

np.random.seed(42)
df = pd.DataFrame({
    "Age": np.random.randint(20, 60, 300),
    "Salary": np.random.randint(20000, 120000, 300)
})

# -------------------- Standardization --------------------
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

# -------------------- Normalization --------------------
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

# -------------------- Graph 1: Original Salary --------------------
plt.figure(figsize=(17,4))
plt.suptitle("Standardization and Normalization Usage")

plt.subplot(1,3,1)
plt.hist(df["Salary"], bins=25)
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

# -------------------- Graph 2: Standardized Salary --------------------
plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"], bins=25)
plt.title("Standardized Salary Distribution (Mean=0, Std=1)")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")

# -------------------- Graph 3: Normalized Salary --------------------
plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"], bins=25)
plt.title("Normalized Salary Distribution (Range 0-1)")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()

# -------------------- Print Samples --------------------
print("Original Data Sample:\n", df.head())
print("\nStandardized Data Sample:\n", df_standardized.head())
print("\nNormalized Data Sample:\n", df_normalized.head())

#print("\n1. StandardScaler Applied:")
#print("   - Data mean is centered at 0")
#print("   - Standard deviation becomes 1")
#print("   - Best suited for algorithms assuming normally distributed data")
#print("   - Used here for SVM because SVM works better when features are centered\n")

#print("2. MinMaxScaler Applied:")
#print("   - Data scaled between 0 and 1")
#print("   - Preserves shape of original distribution")
#print("   - Commonly used in Neural Networks and KNN\n")

print("WHY SCALING IS IMPORTANT:")
print("   - Without scaling, Salary (20000–120000) dominates Age (20–60)")
print("   - Distance-based algorithms (KNN, SVM) rely on Euclidean distance")
print("   - Scaling ensures both features contribute equally\n")