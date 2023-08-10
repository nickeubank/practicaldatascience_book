#!/usr/bin/env python
# coding: utf-8

# # Cleaning Data Types
# 
# In our past two readings, we learned about methods for cleaning our data by modifying the *values* of certain variables. But a second and extremely common data cleanliness problem pertains to managing data *types*. For example, it is very common to load data that you think *should* be numeric (say, `float64`), only to discover that pandas has loaded it as `Categorical` or `Object` type, which means you can't do numeric computations on the data (e.g., `mean`, `median`, etc.). 
# 
# There are two main reasons that this can happen:
# 
# - There are observations that are *accidentally* being parsed as non-numeric, or
# - There are observations that are *deliberately* non-numeric you didn't realize were there.
# 
# Because this is so common, let's look at a quick example of this type of problem with our old friend `world-very-small`! 

# In[6]:


import numpy as np
import pandas as pd
world = pd.read_csv("data/world-very-small-type-errors.csv")
world


# Obviously we can see there are going to be issues with `gdppcap08` and `polityIV`, but this were a real (big) dataset where this wasn't evident and you tried to calculate the average GDP of countries in the data. You would get a *very* weird `ValueError` / `TypeError` that might look something like this (I'm removing most of the stuff in the middle for sanity):
# 
# ```python
# world["gdppcap08"].mean()
# 
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# File ~/opt/miniconda3/lib/python3.9/site-packages/pandas/core/nanops.py:1622, in _ensure_numeric(x)
#    1621 try:
# -> 1622     x = float(x)
#    1623 except (TypeError, ValueError):
#    1624     # e.g. "1+1j" or "foo"
# 
# ValueError: could not convert string to float: '1029635613na855161397271'
# 
# [...]
# 
# File ~/opt/miniconda3/lib/python3.9/site-packages/pandas/core/nanops.py:1629, in _ensure_numeric(x)
#    1626             x = complex(x)
#    1627         except ValueError as err:
#    1628             # e.g. "foo"
# -> 1629             raise TypeError(f"Could not convert {x} to numeric") from err
#    1630 return x
# 
# TypeError: Could not convert 1029635613na855161397271 to numeric
# ```
# 
# What does all this mean? In short, it means that when pandas tried to run `mean()` it realized the method would only work if the data were numeric, so it tried to convert everything in the Series to a numeric type, but it found something in the Series it couldn't convert. Why is the error `TypeError: Could not convert 1029635613na855161397271 to numeric` and not `TypeError: Could not convert na to numeric`? Honestly, I don't have the foggiest notion, but that's what I got with my current version of pandas so I'm gonna leave it in this lesson so you know how weird these things can get!
# 
# But the key take-away is this: what we *can* see is that there was a failure to convert a value to numeric. And that means there's something in our Series that can't be parsed.

# 
# ## Finding Problematic Observations
# 
# So the first thing we can do, as a sanity check, is check the `dtypes` of our dataframe to confirm that what we *thought* was a numeric column is in fact an `object` or `Categorical` column:

# In[3]:


world.dtypes


# Oops! Yup, there it is! Indeed, we can also see that `polityIV` is also an `object`, something we'll deal with later. 
# 
# So this kind of phenomenon is such a common problem that pandas has a tool to deal with it: `.str.isnumeric()`. This method returns `True` is an observation can be converted to a number without issues, and `False` otherwise, so by using its logical negation, we can find all observations that aren't convertible (which we may then need to fix):

# In[4]:


world.loc[~ world["gdppcap08"].str.isnumeric(), "gdppcap08"].value_counts()


# (Recall we have to use `~` instead of `not` to invert `True` values to `False` in a numpy array or pandas Series)
# 
# There we are! One observation of `"na"` is the source of our problems. Note that you could also use `.unique()` instead of `.value_counts()` if you don't care about the number of observations are causing problems. 
# 
# OK, so how do we fix this? In this case, it seems like `na` is probably just short for `np.nan`, so we can replace it with `np.nan`, which *is* a number:

# In[7]:


world.loc[world["gdppcap08"] == "na", "gdppcap08"] = np.nan


# Then we can either cast `gdppcap08` to a numeric type directly with `world["gdppcap08"] = world["gdppcap08"].astype("float")`, or let pandas do it implicitly when we run `world["gdppcap08"].mean()`. In general the former is probably better practice, so let's do that:

# In[8]:


world["gdppcap08"] = world["gdppcap08"].astype("float")
world["gdppcap08"].mean()


# Now, there's one other option in these situations: if `na` is appearing in lots of places in your data as a representation for missing data, we can also communicate this fact to `read_csv`. Remember when we said that `read_csv` has more options than you could ever imagine? Well one is `na_values`, where you can specify how missing data is represented in a dataset. If we use that to tell `read_csv` that `"na"` means data is missing, it'll make this correction on the fly!

# In[10]:


world = pd.read_csv("data/world-very-small-type-errors.csv", na_values="na")
world


# In[11]:


world.dtypes


# In[12]:


world["gdppcap08"].mean()


# Magic!

# ## Deliberate Non-Numerics
# 
# While in the example above `"na"` wasn't really meant to be interpreted as a string, sometimes non-numeric values are inserted into datasets to communicate something important to the user. For example, in this toy example `polityIV` has a non-numeric value:

# In[14]:


world.loc[~world["polityIV"].str.isnumeric()]


# Here, the value is to indicate that the value of policy could be 20 *or any value above 20*. Why might this occur? In this case I've made it up, but in many surveys there will be a maximum value allowed (e.g., some surveys have a top income value they can record). These are called "top-codes", and they are different from the case above because it's not immediately clear what value you should put into the field. You *could* put in 20, but... the value might not be 20, it could be 21!
# 
# So when you find a top-code like this, you need to think carefully about what to do with it, as the answer will depend on the type of analysis you want to do. But the answer will almost always lie not in the data, but in the documentation for the data. 

# ## Review
# 
# - Sometimes data you think should be numeric won't be recognized as numeric by pandas.
# - If you try and do a numeric operation on these columns, you'll get a `TypeError` and/or `ValueError`, and usually a note about an inability to convert some value to numeric.
# - You can confirm that pandas sees a column as non-numeric with `.dtypes`.
# - You can find the non-numeric values with `df[~ df["column"].str.isnumeric(), "column"].value_counts()`. 
# - You can then replace these values with numeric values if it's clear how to do so and recast the column to numeric with `df["column"] = df["column"].astype("float")`.
