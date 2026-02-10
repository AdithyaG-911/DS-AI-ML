# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:12:59 2026

@author: adith
"""

import numpy as np

sensor = np.arange(24)

batch_data = sensor.reshape(4, 3, 2)

transposed_data = batch_data.transpose(0, 2, 1)

print("Final Shape:", transposed_data.shape)
print("\nFinal Array:")
print(transposed_data)