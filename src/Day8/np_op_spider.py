# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:39:40 2026

@author: adith
"""

import numpy as np

#0 dimension array
zero_d=np.array([1])
print(zero_d)

#1 dimension array
one_d=np.array([1,2,3,4,5,6,7,8])
print(one_d)

#2 dimension array
two_d=np.array([[1,4,9],[1,8,27]])
print(two_d)

#3 dimension array
three_d=np.array([[[1,2,3],[2,3,4],[3,4,5]],[[1,2,3],[2,3,4],[3,4,5]]])
print(three_d)

#shape - total elements


# Vectorized vs Loop example
arr = np.random.rand(100)
print(arr)
# Vectorized
squared = arr ** 2
print(squared)

#Reshaping
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

#Horizontal and vertical stack

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)

hstacked = np.hstack((a, b))
print(hstacked)

#Statistical functions in numpy
data = np.array([[10, 20, 30],[40, 50, 60]])

print(np.mean(data))

print(np.mean(data, axis=0)) # column average
print(np.mean(data, axis=1)) #Row average

#Linear Algebra
A = np.array([[1, 2],[3, 4]])

B = np.array([[5, 6],[7, 8]])

print(np.dot(A, B))

arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[1,0,2])

arr=np.arange(0,12,2)
arr3d=arr.reshape(2,3)
print(arr3d)

arr=np.linspace(0,2,5)
print(arr)

arr=np.random.rand(2,3)
arr


arr=np.random.randn(2,3)
arr

arr=np.array([1.2,2.8,-3.7])
print(np.ceil(arr))
