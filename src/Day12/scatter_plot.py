# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 10:58:17 2026

@author: adith
"""

import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.scatter(study_hours,scores)
plt.title("Effect of Study Hours on Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.show()