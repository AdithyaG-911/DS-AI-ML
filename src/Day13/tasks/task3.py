# -*- coding: utf-8 -*-
"""
Goal: Detect multicollinearity and outliers
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('house_prices.csv')

numeric_df = df.select_dtypes(include=['number'])

corr_matrix = numeric_df.corr()

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')

plt.subplot(1, 2, 2)
sns.boxplot(x=df['Price'], color='salmon')
plt.title('Checking for Price Outliers')
plt.xlabel('Price (Million $)')

plt.tight_layout()
plt.show()


print("\n2 Variables with Correlation > 0.8:\n")

count = 0
for i in range(len(corr_matrix.columns)):
    for j in range(i + 1, len(corr_matrix.columns)):
        corr_value = corr_matrix.iloc[i, j]
        if abs(corr_value) > 0.8:
            print(corr_matrix.columns[i], "&",
                  corr_matrix.columns[j],
                  "-> Correlation:", round(corr_value, 2))
            count += 1
        if count == 2:
            break
    if count == 2:
        break

if count == 0:
    print("No variable pairs found with correlation greater than 0.8")

Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Price'] < lower_bound) | (df['Price'] > upper_bound)]

print("\nSome Outliers in Price Column:")
print(outliers['Price'].head())
