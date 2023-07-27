#!/usr/bin/env python
# coding: utf-8

# # Folding and Reshaping Matrices

# To really understand arrays (be they vectors, matrices, or arrays with more dimensions), it helps to understand how arrays are implemented in numpy.
# 
# In numpy, arrays are thought of as a one-dimensional string of entries + information about how that data should be "folded". 
# 
# Why? Because that's how array data is actually laid out in your computer's memory. Computer memory is organized—at least from the perspective of the operating system—in one dimension as a *really* long sequence of spots for storing 1s and 0s. So in a very concrete sense, the data in an array *is* laid out as a one-dimensional string of entries + information about how numpy should "fold" that data when doing operations. 
# 
# The one-dimensional vectors we've been working with, in other words, are just one-dimensional strings of data + information saying they shouldn't be folded. A matrix is a one-dimensional string of data that gets wrapped into rows and columns. That, in fact, is what is stored in `.shape`—directions on how numpy should think about the data being wrapped.
# 
# One consequence of this is that it's very easy to re-fold data in lots of different ways with `numpy`. For example, I can take a 4 x 3 matrix, and make it 3 x 4:

# In[1]:


import numpy as np

my_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
my_matrix


# In[2]:


my_matrix.reshape((3, 4))


# As you can see, numpy thinks of the data in `my_matrix` as all the numbers along one row (the first dimension) followed by the numbers in the second row, etc., and `reshape` is just changing where each row ends and where the next one begins. 

# Indeed, we could also make our data 1 x 12:

# In[3]:


my_matrix.reshape((1, 12))


# But because matrices have to have a regular shape, you can't take any matrix and reshape it into just any shape. Our `my_matrix` above has 12 elements, which means that it can only be reshaped into dimensions that multiply to equal 12, like 1 x 12, 12 x 1, 3 x 4, or 4 x 3. If you tried to use `reshape` to make our matrix, say, 3 x 3, you'd get an error like this:

# ```python 
# my_matrix.reshape((3, 3))
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# /22_reshaping_matrices.ipynb Cell 8' in <cell line: 1>()
# ----> 1 my_matrix.reshape((3, 3))
# 
# ValueError: cannot reshape array of size 12 into shape (3,3)
# ```
# 
# Basically, numpy is saying "Hey, your matrix has 12 elements—if I tried to make it 3 x 3, my matrix would only have space for 9 of those 12 elements, and I wouldn't know what to do with the extra three elements!"

# ### Reshaping Dimensions

# Numpy isn't limited to changing where each row ends and the next one begins, however; it can also change when one *dimension* ends and where the next one begins. So far we've only explicitly worked with one- and two-dimensional arrays, but as we noted before, arrays can organize data along arbitrarily many dimensions. We'll talk about this in detail later, but for the moment, I just want to show you how we can use `reshape` to make our 2-dimensional matrix a 3-dimensional array (namely a 2 x 2 x 3 array):

# In[4]:


my_matrix = my_matrix.reshape((2, 2, 3))
my_matrix


# In[5]:


my_matrix.shape


# So remember: in numpy, an array is always just a string of data that is being folded, and the way the data is folded is indicated by `.shape`, and can always be changed with `.reshape()`.

# ### Reshape and arange

# One place this reshape trick can be very useful is in working with `np.arange()`. Unlike `ones` and `zeros`, to which you can pass the output dimensions you want, `np.arange()` will always return 1-dimensional data. That means that if you want a sequence of numbers in a matrix, you have to combine `np.arange()` with `.reshape()`:

# In[6]:


np.arange(20)


# In[7]:


np.arange(20).reshape((4, 5))


# ### Transpose
# 
# OK, one other cool trick that's related to reshape that often comes up when working with `np.arange()`: `.transpose()`. The transpose of a matrix is what you get when you make rows into columns and columns into rows. For example:

# In[8]:


my_matrix = np.array([[1, 2, 3], [4, 5, 6]])
my_matrix


# In[9]:


my_matrix.transpose()


# Transpose is often combined with `np.array()` and `.reshape()` because otherwise, those two tools would always generate sequences that increase incrementally across rows before wrapping to the next row:

# In[10]:


np.arange(6).reshape((2, 3))


# So if you want your sequence to move down your *columns* instead of across your *rows*, you have to transpose your result:

# In[11]:


np.arange(6).reshape((2, 3)).transpose()


# Indeed, `.transpose()` is so frequently used in numpy that you can call it with `.T`:

# In[12]:


np.arange(6).reshape((2, 3)).T


# ## Exercises 
# 
# 1. Using `np.arange`, create a vector with all the integers from 0 to 23. 
# 2. Using `.reshape`, convert that vector into a matrix with 4 rows and 6 columns where the numbers increase as you move from left to right along each row before wrapping to the next row.
# 3. Using `reshape`, try to convert this matrix into a 5 x 5 matrix. Why were you unsuccessful?
# 4. Using `np.arange`, create a *new* sequence that you *can* reshape into a 5 x 5 matrix.
