# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:45:13 2026

@author: adith
"""

import pandas as pd

df=pd.read_csv('places.csv')
print("Original Data:\n",df)

df['Location']=df['Location'].str.strip()
df['Location']=df['Location'].str.lower()
print("\nData After Cleaning :\n",df)

print("\n---Unique Locations After Cleaning ---")
unique_locations = df['Location'].unique()
print(unique_locations)

