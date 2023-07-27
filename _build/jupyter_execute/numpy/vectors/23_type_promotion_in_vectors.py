#!/usr/bin/env python
# coding: utf-8

# # Type Promotion in numpy

# There's one last lesson that's worth learning about vectors, because it can get you in trouble. 
# 
# As noted above, vectors can only contain one type of data, but if you try pass a list with different kinds of data to `np.array`, numpy will try and be clever and *find* a way to put all that data in one array by doing something called "Type Promotion." Type promotion is the practice of converting all the data you give it to the same type. For example, if I tried to create a vector by combining a string vector and a numeric vector, numpy would convert the numeric value to a string so all the data could fit in a string vector:
# 

# In[1]:


import numpy as np
np.array(["Nick", 42])


# Why did numpy convert `42` to `"42"` and not convert `"Nick"` to a numeric type? Well because `"Nick"` can't be represented as a numeric type in any meaningful sense while any number (like `42`) can always be represented as a character in a meaningful way.
# 
# Indeed, there's a hierarchy of data types, where a type lower on the hierarchy can **always** be converted into something higher in the order, but not the other way around. That hierarchy is:
# 
# `Boolean` --> `integer` --> `float` --> `string`
# 
# When Python is asked to combine data of different types, it will try to move things up this hierarchy by the smallest amount possible in order to make everything the same type.
# 
# (Note there are individual cases that can move backwards -- the character `"5"` could logically be turned into `5` -- but you can't always convert a character to a numeric, so for consistently Python only moves in directions that are **always** possible. 
# 
# For example, if you combine `Boolean` and `float` vectors, Python will convert all of the data into `float` (Remember from our previous reading that Python thinks of `True` as being like `1`, and `False` as being like `0`).
# 

# In[2]:


np.array([1, 2.4, True])


# But it **doesn't** convert that data into a `string` vector (even though it could!) because it's trying to make the smallest movements up that hierarchy that it can. 
# 
# But if we try to combine `Boolean`, `float`, *and* `string` data, Python would be forced to convert everything into a `string` vector:

# In[3]:


np.array([True, 42, "Julio"])


# ## Exercises
# 
# 1. Now we are going to create a vector with the numbers `42`, `47`, and `1.618`. Before you create it, what do you think the `dtype` will be?
# 2. Now create the vector and check your intuition!
# 3. Now we are going to create a vector from the list `[47, True, 3.14]`. Before you create it, what do you think the `dtype` will be? What do you think the array will look like?
# 4. Now create the vector and check your intuition!
# 
