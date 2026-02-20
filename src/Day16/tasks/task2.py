import pandas as pd
import numpy as np

np.random.seed(42)

normal_scores = np.random.normal(loc=75, scale=3, size=200)

data = {
    "Student": [f"S{i}" for i in range(1, 203)],
    "Score": np.concatenate([normal_scores, [120, 30]])
}

df = pd.DataFrame(data)

mu = df["Score"].mean()
sigma = df["Score"].std()

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

df["z_score"] = (df["Score"] - mu) / sigma


outliers = df[np.abs(df["z_score"]) > 3]

print("\nDataset with Z-Scores:")
print(df)

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
