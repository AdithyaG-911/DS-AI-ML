# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:38:39 2026

@author: adith
"""

import pandas as pd

df = pd.read_csv('sales_data.csv')
print(df)

print("--- Initial Data Types ---")
print(df.dtypes)
print("-" * 30)

# 2. Clean 'Price' column: remove '$' and convert to float
df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float)

# 3. Convert 'Date' column to true datetime object
df['Date'] = pd.to_datetime(df['Date'])

print("Final Data:\n",df)

# 4. Verify the changes
print("\n--- Updated Data Types ---")
print(df.dtypes)
print("-" * 30)
