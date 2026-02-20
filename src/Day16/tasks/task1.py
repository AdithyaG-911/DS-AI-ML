import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)


# 1. Human Heights (Normal)
heights = np.random.normal(loc=170, scale=7, size=1000)

# 2. Household Incomes (Right-Skewed)
incomes = np.random.lognormal(mean=10, sigma=0.5, size=1000)

# 3. Easy Exam Scores (Left-Skewed)
scores = 100 - np.random.lognormal(mean=2.5, sigma=0.4, size=1000)
scores = np.clip(scores, 0, 100)  # keep within 0–100

# Put into DataFrame
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

# ---------- Plot Histograms with KDE ----------

plt.figure(figsize=(15, 4))

datasets = ["Heights", "Incomes", "Scores"]

for i, col in enumerate(datasets, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[col], kde=True, bins=30)
    
    mean = df[col].mean()
    median = df[col].median()
    
    plt.axvline(mean, color='r', linestyle='--', label=f"Mean={mean:.1f}")
    plt.axvline(median, color='g', linestyle='-', label=f"Median={median:.1f}")
    
    plt.title(col)
    plt.legend()

plt.tight_layout()
plt.show()

# ---------- Print Mean vs Median ----------

for col in datasets:
    mean = df[col].mean()
    median = df[col].median()
    
    print(f"{col}: Mean = {mean:.2f}, Median = {median:.2f}")
    
    if mean > median:
        print("→ Right-Skewed\n")
    elif mean < median:
        print("→ Left-Skewed\n")
    else:
        print("→ Approximately Normal\n")
