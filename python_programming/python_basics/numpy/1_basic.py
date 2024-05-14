# https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp

# https://www.edureka.co/blog/python-numpy-tutorial/

import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# *****************

# Access 2-D Arrays

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])

# *******************


# NumPy Array Slicing

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

# output
# [2 3 4 5]

# ********************

# Python NumPy Operations

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)  # Output – int32
print(a.size)  # 6
print(a.shape)  # (2, 3)


a = np.array([(8, 9, 10), (11, 12, 13)])
print(a)
a = a.reshape(3, 2)
print(a)
