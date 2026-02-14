# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 11:01:39 2026

@author: adith
"""

import matplotlib.pyplot as plt
categories=['Electronics','Clothing','Home']
values=[300,450,200]

plt.suptitle("Comparision of Sales")
plt.subplot(1,2,1)
plt.bar(categories,values)
plt.title("Bar Graph")
plt.xlabel("categories")
plt.ylabel("Sales")

plt.subplot(1,2,2)
plt.scatter(categories,values)
plt.title("Scatter Plot")
plt.xlabel("categories")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()