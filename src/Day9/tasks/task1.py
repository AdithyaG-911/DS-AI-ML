# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:24:15 2026

@author: adith
"""

import pandas as pd

products=pd.Series([47000,12000,300],index=['Laptop','Mobile','Charger'])
print("Full Series :\n",products)

print("\nLaptop Price: ",products['Laptop'])
print("\nFirst two products :\n",products[:2])
