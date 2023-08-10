#!/usr/bin/env python
# coding: utf-8

# # Intro to Matrices

# 
# Matrices are a natural extension of the vectors that we have been working with in the last couple reading; where a vector is a collection of data of the same type ordered along a *single* dimension, a matrix is a collection of data of the same type ordered along *two* dimensions.
# 
# If you've taken a linear algebra course before, the idea of a matrix will be very familiar, but if you haven't, don't fret! You can also think of a matrix as either (a) a collection of vectors lined up side-by-side, or, if it feels more familiar, (b) an Excel spreadsheet with data arranged in rows and columns. For example a 3x3 matrix might look something like:
# 
# $$
# \begin{bmatrix} 
# 1 & 2 & 3 \\
# 4 & 5 & 6 \\
# 7 & 8 & 9 \\
# \end{bmatrix}
# \quad
# $$
# 
# Just as vectors are commonly used in data science because we usually don't just have a single observation of data, but instead lots of observations (different customers) that we might want to put into vector, so too do we often have information not just on one type of measurement (amount of last purchase), but lots of different measurements about each observation (weeks since first purchase, weeks since last purchase, total spent over customer lifetime). Matrices are commonly used to represent this type of data by using each row for an observation (a customer), and each column for a different thing were measuring.
# 
# For example, suppose we were conducting an opinion survey, and we surveyed four people. Further, suppose our first respondent was twenty years old, had an income of 22,000 dollars, and twelve years of education, the second respondent was thirty-five years old, had an income of 65,000 dollars, and sixteen years of education, and the third and fourth respondents were fifty-five and forty-five years old, had incomes of 19,000 and 35,000 dollars, and had eleven and twelve years of education, respectively. We could represent that information in a matrix that looks like:
# 
# $$
# \begin{bmatrix} 
# 20 & 22,000 & 12 \\
# 35 & 65,000 & 16 \\
# 55 & 19,000 & 11 \\
# 45 & 35,000 & 12 \\
# \end{bmatrix}
# \quad
# $$
# 
# And while it may not be immediately obvious why, this way of representing our data will turn out to not only be a useful organizational scheme, but also be incredibly valuable for statistical analyses.
# 
# ## Why Learn About Matrices?
# 
# There are (at least) four reasons to learn about matrices as a data scientist. The first is that a matrix is one of the standard ways that we organize tabular data -- data where each row is a different *observation* or *individual unit* we are studying, and each column is a different property about which we have data for those observations. So we'll use matrices directly a lot. 
# 
# The second is that matrices are a natural steppingstone from vectors to arrays of arbitrary dimension (N-D arrays), as well as another data structure we'll work with a lot: pandas `DataFrames`. So everything we learn here will be immediately applicable in our following lessons.
# 
# The third is that matrices are also the standard way we represent image data, which is also commonly used by data scientists interested in computer vision and image processing. A picture is just a grid of pixels, each containing information about the color containing in that pixel. Matrices are the natural way to represent this type of gridded data, so as we'll see below we can easily represent images as matrices. 
# 
# And the fourth reason is that matrices (and linear algebra, the mathematics of matrices) underlie nearly all the statistical models that we use in data science (like linear regression, logistic regression models, SVMs, etc.). So when we begin to work with statistics and machine learning packages, matrices will be inescapable.

# ## Constructing Matrices
# 
# As with vectors, there are several ways of constructing matrices. 
# 
# The first is simply passing lists of lists to `np.array`. For example, here we can create the matrix of survey responses we talked about above by putting each row into a list, then putting those lists into a bigger list and passing it to `np.array`. This will give use our matrix where each row represents a different person, and the columns represent respondent age, income, and years of education. 
# 

# In[2]:


import numpy as np

survey = np.array(
    [[20, 22_000, 12], [35, 65_000, 16], [55, 19_000, 11], [45, 35_000, 12]]
)

survey


# Great! We can already see from how this has been printed out that this is a matrix with four rows and three columns, but we can also verify this directly by checking the `.shape` attribute of our matrix:

# In[3]:


survey.shape


# As we can see, `.shape` reports that our matrix has four rows (the first entry) and three columns (the second entry). Moreover, the fact we see two entries is what tells us that this is a 2-dimensional array.

# In addition, we can also build matrices with the tools like `ones` and `zeros` we saw before by specifying the size of the result we want with a tuple containing the number of rows and the number of columns we want in the result:

# In[4]:


np.ones((2, 5))


# In[5]:


np.zeros((4, 2))


# (As with vectors, the `.` appearing after the `1`s and `0`s above is numpy's way of telling us that these are arrays of floats, not integers, even though these numbers could be stored as integers.)

# ### Typing
# 
# As with vectors, all the entries in a matrix must be of the same type—in other words, matrices are a *homogenously typed* data structure. And as with vectors, we can check the types of our matrices using `.dtype`:
# 

# In[7]:


survey.dtype


# In[8]:


np.ones((2, 5)).dtype


# ## Math with Matrices
# 
# Just like vectors, we can use matrices to do math in especially efficient ways.
# 
# Suppose, for example, we had a dataset of with the salaries of three people where the first column is each person's salary before they got a technical certification, and the second column is each person's salary after receiving the technical certification: 

# In[6]:


salaries = np.array([[30_000, 37_000], [42_000, 45_000], [22_000, 29_000]])
salaries


# Now suppose I wanted to convert these salaries in dollars to salaries in thousands of dollars to make the table easier to fit on a graph. I can just do:

# In[7]:


salaries_in_thousands = salaries / 1000
salaries_in_thousands


# Similarly, matrices can be added if they have the same size. If we also had a matrix of tax refunds, and we wanted to calculate everyone's total after-tax incomes, we could just add the matrices:

# In[8]:


refunds = np.array([[5_000, 3_000], [4_000, 4_000], [8_000, 7_000]])
refunds


# In[9]:


total_income = salaries + refunds
total_income


# Of course, we won't always want to do full-matrix manipulations -- for example, we might want to adjust one income column for inflation to ensure the two incomes are comparable. Manipulating *subsets* of matrices (such as individual rows, columns, or entries) is something we'll discuss in detail in our next reading. 

# ## Exercises 
# 
# 1. Using `np.array`, create a new matrix with two rows and three columns. In the first row, place information about yourself, and in the second row place information about a good friend. In the first column enter your ages, in the second column enter an estimate of your current income rounded to the nearest thousand, and in the third column add a `1` if you identify as a woman and a `0` otherwise.
# 2. Confirm the shape of your matrix with `.shape`.
# 3. What data type is your matrix?
# 4. Without writing any code, what data type matrix do you think you would get if, instead of rounding your income to the nearest thousand, you entered your income to the nearest cent (or your local currency's decimal equivalent—Indian paise, British pence, etc.)?
# 5. Check your answer to number 4 above in Python.
