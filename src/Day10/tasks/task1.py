# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:19:57 2026

@author: adith
"""

import pandas as pd

df=pd.read_csv('customer_orders.csv')
print(df)

shape_before = df.shape

print("--- Missing Values Report ---")
print(df.isna().sum())
print("-" * 30)

numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

df = df.drop_duplicates()

print("Cleaned Data:\n",df)
shape_after = df.shape

print("\n--- Cleaning Summary ---")
print(f"Shape Before Cleaning : {shape_before} (Rows, Columns)")
print(f"Shape After Cleaning  : {shape_after} (Rows, Columns)")
print(f"Total Rows Removed    : {shape_before[0] - shape_after[0]}")
print("-" * 30)