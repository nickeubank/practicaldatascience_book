#!/usr/bin/env python
# coding: utf-8

# # Editing Subsets

# Sometimes we want to modify a *part* of a matrix. For example, suppose we were working with our survey data, and we want to multiply all the income values by `1.02` to adjust for inflation that has occurred since the survey. Obviously, if we just multiplied the matrix by `1.02`, we'd also modify things like education and age:

# In[1]:


import numpy as np


survey = np.array(
    [[20, 22_000, 12], [35, 65_000, 16], [55, 19_000, 11], [45, 35_000, 12]]
)

survey


# In[2]:


survey * 1.02


# What we can do instead is extract the column with income, modify it, then replace the old income column with our updated column:

# In[3]:


income_column = survey[:, 1]  # Extract income
adjusted_income = income_column * 1.02  # Adjust income
survey[:, 1] = adjusted_income  # Replace income with new values!
survey


# Or, if we wanted, we could actually do all this in one step:

# In[4]:


# Re-make survey so it hasn't been adjusted for inflation
survey = np.array(
    [[20, 22_000, 12], [35, 65_000, 16], [55, 19_000, 11], [45, 35_000, 12]]
)


# In[5]:


# Now adjust income in one step!
survey[:, 1] = survey[:, 1] * 1.02
survey


# And this is *especially* powerful if we subset on BOTH rows and columns. Suppose, for example, we wanted to see what people's incomes would look like if anyone who didn't finish high school (`education < 12`) got a tax credit of 10,000 dollars:

# In[6]:


survey[survey[:, 2] < 12, 1] = survey[survey[:, 2] < 12, 1] + 10000


# In[7]:


survey


# ## Views and Copies with Matrices
# 
# When it comes to views and copies, the same rules apply to matrices as applied to vectors: if you create a subset through simple indexing, the result will be a view; if you create a subset by a different method, you get a copy!

# And that's it! Now you're a matrix pro. 

# ## Exercises
# 
# 1. Using `np.arange`, create a 3 x 5 matrix with all the numbers from 0 to 14. Assignment to the variable `my_matrix`.
# 2. Subset the third and fourth columns of the matrix (the columns starting with 2 and 3) with simple indexing. Assign the subset to the variable `m2`.
# 3. Change the top, left-most element of your new matrix `m2` to `-99`.
# 4. Without running any code, try and predict what `my_matrix` currently looks like.
# 5. Now check `my_matrix`—does it look how you expected? Why or why not?
