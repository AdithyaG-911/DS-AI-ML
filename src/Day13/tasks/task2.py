# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 11:26:17 2026

@author: adith
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame(pd.read_csv('house_prices.csv'))

plt.figure(figsize=(14, 6))

# Subplot 1: Scatter Plot
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='Square_Footage', y='Price', hue='City', alpha=0.7)
plt.title('House Price vs. Square Footage')
plt.xlabel('Square Footage (sq ft)')
plt.ylabel('Price (Millions of $)')

# Add a trend line to see the overall direction
sns.regplot(data=df, x='Square_Footage', y='Price', scatter=False, color='red')

# Subplot 2: Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='City', y='Price', hue='City', palette='Set2', legend=False)
plt.title('Price Distribution by City')
plt.xlabel('City')
plt.ylabel('Price (In Millions $)')

plt.tight_layout()
plt.show()

print("As Square_Footage increases, Price seems to increase.")