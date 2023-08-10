#!/usr/bin/env python
# coding: utf-8

# # Matrix Exercises
# 
# For the following matrix manipulation exercises, begin by building the following matrix (you'll probably want to just copy-paste this code), which we can imagine is a survey of income (first column), age (second column), and years of education (third column):

# In[1]:


import numpy as np

svy = np.array(
    [
        [22_000, 20, 12],
        [65_000, 35, 16],
        [19_000, 55, 11],
        [11_0000, 35, 22],
        [14_000, 21, 12],
        [0, 56, 8],
        [35_000, 42, 12],
    ]
)
svy


# ## Part 1: Summarizing Data
# 
# 1. What is the average age of all respondents?
# 2. What is the average income of respondents over 30?
# 3. What is the average education of respondents with incomes above the average income for all respondents?
# 
# ## Part 2: Editing Data
# 
# The US government is thinking about offering a 1,500 tax credit to anyone making less than 20,000 a year. 
# 
# 1. Using the data from `svy`, create a new vector by subsetting and editing the original income column with the incomes respondents will receive after this tax credit.
#     - Do so by subsetting and editing values programmatically, *not* just typing values by hand. (Yes, writing out a new vector by hand is easy to do in this example, but you couldn't do it with a large, real dataset!)
#     - Do **not** change the original income column in the process of creating this vector.
# 
# 2. What will the average after-tax income be for all respondents?
# 
# 3. Add your new column with updated, post-refund incomes as a fourth column in your matrix.
# 
# To solve this problem, you'll want to use the `np.hstack` function. As detailed in the [numpy documentation](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html) (seriously, go take a look—numpy documentation is really good and helpful!), `hstack` concatenates ("stacks") arrays horizontally to make new arrays. Just put the arrays you want to concatenate in a list (they must have the same number of rows!) and pass them to `hstack`:
# 

# In[2]:


import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array1


# In[3]:


array2 = np.array([[-10, -11], [-98, -99]])
array2


# In[5]:


np.hstack([array1, array2])


# (There's also a function called `np.vstack` to stack matrices or arrays vertically). 
# 
# Hint: `hstack` will only concatenate arrays with the same number of dimensions and same number of rows!
# 
# 4. How much will this tax refund cost the government (in other words, how much will the government have to pay out / how much will total incomes increase?)
# 
# Hint: One way to do this involves `np.sum()`.

# ## Solutions

# ### Part 1

# In[1]:


import numpy as np

svy = np.array(
    [
        [22_000, 20, 12],
        [65_000, 35, 16],
        [19_000, 55, 11],
        [11_0000, 35, 22],
        [14_000, 21, 12],
        [0, 56, 8],
        [35_000, 42, 12],
    ]
)
svy


# In[2]:


# Question 1
np.mean(svy[:,1])


# In[3]:


# Question 2
np.mean(svy[svy[:,1] > 30, 0])


# In[4]:


# Question 3
avg_income = np.mean(svy[:, 0])
np.mean(svy[svy[:, 0] > avg_income, 2])


# ### Part 2

# In[6]:


# Question 1
after_tax_incomes = svy[:, 0].copy()
incomes_under_20_000 = after_tax_incomes < 20_000
after_tax_incomes[incomes_under_20_000] = after_tax_incomes[incomes_under_20_000] + 1_500
after_tax_incomes


# In[7]:


svy[:, 0]


# In[ ]:


# Question 3
np.mean(after_tax_incomes)


# In[10]:


# Question 4
new_matrix = np.hstack([svy, after_tax_incomes.reshape((7, 1))])
new_matrix


# In[12]:


np.sum(new_matrix[:, 3] - new_matrix[:, 0])

