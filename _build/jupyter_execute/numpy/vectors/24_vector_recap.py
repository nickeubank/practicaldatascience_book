#!/usr/bin/env python
# coding: utf-8

# # Vector Recap
# 
# - Numpy is the workhorse of data science in Python. Numpy is not only orders of magnitude faster than vanilla Python, but it uses memory much more efficiently, 
# - Vectors are collections of data *of the same type*. 
# - Simple vectors can be easily created by passing a list to the `np.array()` function, or by using the `np.arange()` function the same way you would use `range()`.
# - You can easily do math between any vector and a scalar/vector of length 1. The operation will just be repeated for each entry in the longer vector.
# - You can also easily do math between a vector and another vector of the same length. Entries in the two vectors will just be matched up pair-wise.
# - If data of different types are passed to the `np.array()` function, `numpy` will type promote them to the lowest type that can store all the input types.

# ## Next Steps
# 
# Now that we're familiar with vectors, [let's do some exercises!](25_EX_vectors.ipynb)
