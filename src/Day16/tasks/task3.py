import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# ---------- Step 1: Create Skewed Dataset ----------
# Lognormal distribution simulates income (right-skewed)
data = np.random.lognormal(mean=10, sigma=0.8, size=100000)

# ---------- Step 2: Sampling ----------
sample_means = []

for _ in range(1000):
    sample = np.random.choice(data, size=30)
    sample_means.append(sample.mean())

sample_means = pd.Series(sample_means)

# ---------- Step 3: Plot ----------
plt.figure(figsize=(12,5))

# Original skewed data
plt.subplot(1,2,1)
sns.histplot(data, bins=50, kde=True)
plt.title("Original Data (Right-Skewed)")

# Distribution of sample means
plt.subplot(1,2,2)
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (≈ Normal)")

plt.tight_layout()
plt.show()