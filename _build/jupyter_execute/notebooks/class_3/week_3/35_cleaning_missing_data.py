#!/usr/bin/env python
# coding: utf-8

# # Missing Data
# 
# In our previous reading, we encountered a situation in which observations of total income (`inctot`) in our US American Community Survey data were set to `9999999` for children as a way of indicating that there was no meaningful data available for that group. And while using special numbers—Sentinel Values—to denote a lack of data / missing data is increasingly uncommon, missing data itself is not. There are endless situations in which we want to deliberately communicate that data is unavailable for specific observations. For example, someone taking a survey may have refused to answer certain questions, or a sensor on an industrial machine may have failed to record data for a specific period due to a wiring issue. 
# 
# In those situations, we have two main options for indicating an observation is missing in Python: 
# 
# - `np.nan`: The most common is the "Not a Number" object in the numpy library: `np.nan`. `np.nan` is actually a specific value that can be taking by floating point numbers, so a `np.nan` value can appear in a numeric Series without causing problems. 
# - `None`: The other way for denoting a missing value is the Python `None` object. As `None` is a Python object, it can only be used in a Series with an `object` datatype. 
# 
# While `np.nan` and `None` look like normal entries in a pandas Series or DataFrame, they do exhibit some odd behavior to be aware of. 
# 
# First, as happens with missing values in many languages, `np.nan == np.nan` will always return false:
# 

# In[10]:


import numpy as np

np.nan == np.nan


# This isn't true for `None`, as `None == None` does return `True`, but as a Data Scientist you'll see `np.nan` more often than `None` since it can represent missing data in a numeric Series.

# This can cause problems if, for example, you wanted to get all the rows of a DataFrame with missing values. To illustrate, suppose our small world dataset didn't have data for Mozambique (the value was `np.nan`):

# In[11]:


import pandas as pd

smallworld = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-very-small.csv"
)
smallworld.loc[smallworld.country == "Mozambique", "polityIV"] = np.nan
smallworld


# Now suppose we wanted to get all the rows with missing polity scores. The natural way to do this would be:

# In[12]:


smallworld.loc[smallworld.polityIV == np.nan]


# But as we can see, this doesn't work! Why? Because even when the actual value in the DataFrame *is* `np.nan`, `np.nan == np.nan` doesn't return `True`, and so we don't get any rows. 
# 
# To deal with this, pandas offers two utility functions: `pd.isnull(np.nan)` and `pd.notnull(np.nan)` that you can use. So for example, to get rows with no polity scores, we'd run:

# In[13]:


smallworld.loc[pd.isnull(smallworld.polityIV)]


# Or we can use it as a method too:

# In[14]:


smallworld.loc[smallworld.polityIV.isnull()]


# `pd.isnull()` also has the advantage of working the same with both `None` and `np.nan`, as:

# In[15]:


pd.isnull(None)


# So if, for example, our data didn't have a polity score for Mozambique but we just learned what it should be, we could edit that specific value with:

# In[16]:


smallworld.loc[smallworld.polityIV.isnull(), "polityIV"] = 5
smallworld


# ## Missing Data and .value_counts()
# 
# One important thing to flag is that the `.value_counts()` tool we introduced in our data cleaning exercise will, by default, *ignore* missing values when it provides a list of all unique values and their frequencies. So if, for example, our American Community Survey data used `np.nan` instead of `n/a` for missing values of the employment status, `.value_counts()` would do the following:

# In[19]:


acs = pd.read_stata(
    "https://github.com/nickeubank/MIDS_Data/blob/master"
    "/US_AmericanCommunitySurvey/US_ACS_2017_10pct_sample.dta?raw=true"
)

acs.loc[acs["empstat"] == "n/a", "empstat"] = np.nan
acs["empstat"].value_counts()


# While this can be a useful behavior, sometimes we want to know about observations with missing values. In those situations, you have to pass the `dropna=False` keyword argument to `value_counts()`:

# In[21]:


acs["empstat"].value_counts(dropna=False)


# ## Other Missing Data Tools

# In addition to `pd.isnull()` and `pd.notnull()`, pandas also has some additional missing value tools that you may find useful:

# - `.fillna(x)`: Replace missing values with the value of `x`
# - `.dropna()`: Drop rows with missing values.
# - `.count()`: Returns the number of NON-MISSING observations. 

# And that's how, once we've found problems, we can fix problems in our data!

# ## Review:
# 
# - Long ago, people represented missing data using "Sentinel Values"—numeric values unlikely to occur naturally, like `9999999`.
# - Today, Python has two representations of missing data: `np.nan`, which is a special value of floating point numbers, and `None`, which is a Python object. 
# - A special characteristic of `np.nan` is that `np.nan == np.nan` will always return `False`, so to subset for missing observations, one must use `pd.isnull()` or `pd.notnull()`, not `== np.nan` or `!= np.nan`. 
# - This is not true of `None`, as `None == None` returns `True`, but as a data scientist you're likely to encounter `np.nan` more than `None`.
# - Moreover, `pd.isnull()` and `pd.notnull()` treat `np.nan` and `None` identically.
# - `.value_counts()` will only report the number of observations that are missing if you use `.value_counts(dropna=False)`.
