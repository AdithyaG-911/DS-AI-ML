# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:53:29 2026

@author: adith
"""

import numpy as np

scores=np.random.randint(50,101,size=(5,3))
print(f"Original Scores: \n{scores}")

means=np.mean(scores,axis=0)

print("\nSubject Means:")
for i, sub_mean in enumerate(means):
    print(f"Subject {i+1}: {sub_mean:.2f}")

broadcast_score=scores-means
print(f"\nCentered Scores :{broadcast_score}")
