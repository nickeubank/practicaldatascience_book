#!/usr/bin/env python
# coding: utf-8

# # Views and Copies Exercises
# 
# **Note**: 
# 
# > This exercise has been written out in something called a Jupyter Notebook. We'll discuss Jupyter Notebooks in more detail later in the course—they are very a powerful tool for data science communication!—but for the time being, the notebook is just a convenient way for us to write out the exercise. You don't need to *do* anything with the notebook except read its contents.
# 
# 
# Unlike many of our previous exercises, you should first attempt to complete these exercises with pen and paper, **not** using an active Python session. This will give you an opportunity to test your understanding of how views and copies work in Python. If at any point you realize you aren't certain how views and copies behave in a given situation, please revisit the previous readings to renew your understanding. 
# 
# Only when explicitly prompted should you open an active Python session to check your answers.
# 
# ## Exercise 1
# 
# Suppose we begin with the following array:
# 
# ```python
# import numpy as np
# 
# my_array = np.array([1, 2, 3, 4, 5])
# print(my_array)
# 
# [1 2 3 4 5]
# ```
# 
# 
# If we were to then run:
# 
# ```python
# my_slice = my_array[1:3]
# ```
# 
# What is the current value of `my_slice` after running that code?
# 
# ## Exercise 2
# 
# Now suppose we run:
# 
# ```python
# my_array = np.array([1, 2, 3, 4, 5])
# my_slice = my_array[1:3]
# my_array = my_array * 2
# ```
# 
# What is the current value of `my_slice` after running that code?
# 
# ## Exercise 3
# 
# Now suppose we run:
# 
# ```python
# my_array = np.array([1, 2, 3, 4, 5])
# my_slice = my_array[1:3]
# my_array[:] = my_array * 2
# ```
# 
# What is the current value of `my_slice` after running that code?
# 
# ## Exercise 4
# 
# Stop, open Python, and try running these examples. Were your predictions correct? If not, why not?
# 
# ## Exercise 5
# 
# OK, now close Python again and return to writing your answers with pen and paper.
# 
# Now suppose we run:
# 
# ```python
# my_array = np.array([1, 2, 3, 4, 5])
# my_slice = my_array[1:3].copy()
# my_array[:] = my_array * 2
# ```
# 
# What is the current value of `my_slice` after running that code? (Notice that line two of the code has changed since Exercise 3).
# 
# ## Exercise 6
# 
# Now suppose we run:
# 
# ```python
# my_array = np.array([1, 2, 3, 4, 5])
# my_slice = my_array[[1, 2]]
# my_array[:] = my_array * 2
# ```
# 
# What is the current value of `my_slice` after running that code? (Notice that line two of the code has changed since Exercise 5).
# 
# ## Exercise 7
# 
# Stop, open Python, and try running these examples. Were your predictions correct? If not, why not?
# 
# ## Exercise 8
# 
# Now suppose we run:
# 
# ```python
# my_array = np.array([1, 2, 3, 4, 5])
# my_slice = my_array[1:3]
# my_slice[0] = -99
# ```
# 
# What is the current value of `my_array` after running that code?
# 
# ## Exercise 9
# 
# Now suppose we run:
# 
# ```python
# my_array = np.array([1, 2, 3, 4, 5])
# my_slice = my_array[1:3]
# my_array = my_array * 2
# my_slice[0] = -99
# ```
# 
# What is the current value of `my_array` after running that code?
# 
# ## Exercise 10
# 
# Stop, open Python, and try running these examples. Were your predictions correct? If not, why not?

# 
