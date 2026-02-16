import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('house_prices.csv')
df=pd.DataFrame(data)

plt.figure(figsize=(14, 6))
plt.suptitle("Price Distribution and City Count")
# Subplot 1: Histogram with KDE
plt.subplot(1, 2, 1)
sns.histplot(df['Price'], kde=True, color='skyblue', bins=20)
plt.title('Distribution of House Prices')
plt.xlabel('Price (Millions of $) ')
plt.ylabel('Frequency')

# 2. Calculate Skewness and Kurtosis
price_skew = df['Price'].skew()
price_kurt = df['Price'].kurt()

print(f"Skewness: {price_skew:.2f}")
print(f"Kurtosis: {price_kurt:.2f}")

plt.subplot(1, 2, 2)
sns.countplot(data=df, x='City', hue='City', palette='viridis', legend=False)
plt.title('Number of Houses per City')
plt.xlabel('City')
plt.ylabel('Count')

plt.tight_layout()
plt.show()