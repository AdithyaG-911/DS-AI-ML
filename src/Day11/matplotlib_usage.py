# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 10:20:20 2026

@author: adith
"""
#Matplotlib basic usage
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 11]

plt.plot(x, y)
plt.show()

#Scatter plot

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.scatter(x, y)
plt.show()

#Bar Chart

categories = ['A', 'B', 'C']
values = [11, 20, 15]

plt.bar(categories, values)
plt.show()

#Customization using sub-plots

plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")
plt.subplot(1, 2, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()