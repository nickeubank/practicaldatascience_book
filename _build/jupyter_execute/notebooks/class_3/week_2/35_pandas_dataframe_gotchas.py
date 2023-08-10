#!/usr/bin/env python
# coding: utf-8

# # Subsetting DataFrame Tricks and Gotchas
# 
# Two features of subsetting DataFrames are worth special attention: subsetting with simple square brackets (`[]`), and subsetting columns with dot-notation.
# 

# In[1]:


import pandas as pd

world = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-small.csv"
)
world


# ## `[]` Square brackets
# 
# As with Series, single square brackets in `pandas` change their behavior depending on the values you pass them. Again, it is worth emphasizing that there is *nothing* that one can do with square brackets that you can't do with `.loc` and `.iloc`, so if they seem to strange, you don't have to use them. 
# 
# With that said, as summarized below, `[]` is actually much safer on DataFrames than on Series. 
# 
# The rules of `[]` in DataFrames are:
# 
# - If your entry is a *single* column name, or a list of column names, it will return those columns. 
# - If your entry is a slice, it will work like `iloc` and select rows based on row order. 
# - If your entry is a Boolean array, *and* of exactly the same length as the number of rows in your data, it will subset rows.

# In[2]:


# Select one column
world["country"].head()


# In[3]:


# Select multiple columns
world[["country", "gdppcap08"]].head()


# In[4]:


# Boolean test
world[world["gdppcap08"] > 10000].head()


# In[5]:


# Slice of rows
world[0:3]


# ## My advice on using `[]` on DataFrames
# 
# `[]` is much safer on DataFrames because the situation we saw with Series where `[]` *might* subset on index labels (if your index labels are integers) or it *might* subset on row order (if your index labels are not integers) doesn't exist. Moreover, selecting a single column is *extremely* common, and this is a case where I use single square brackets all the time.
# 
# In a Series, if I pass `0`, it's always unclear whether that's going to get me the first row (row-order-based) or the row with index value 0 (if I have integer index values). 
# 
# On a DataFrame, a single entry or list of entries will *only* attempt to match columns based on index values, and if that fails, it throws an exception rather than defaulting to acting like `.iloc`:

# ```python
# 
# world[0]
# 
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/core/indexes/base.py:3652, in Index.get_loc(self, key)
#    3651 try:
# -> 3652     return self._engine.get_loc(casted_key)
#    3653 except KeyError as err:
# 
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/_libs/index.pyx:147, in pandas._libs.index.IndexEngine.get_loc()
# 
# File ~/opt/miniconda3/lib/python3.10/site-packages/pandas/_libs/index.pyx:176, in pandas._libs.index.IndexEngine.get_loc()
# 
# File pandas/_libs/hashtable_class_helper.pxi:7080, in pandas._libs.hashtable.PyObjectHashTable.get_item()
# 
# File pandas/_libs/hashtable_class_helper.pxi:7088, in pandas._libs.hashtable.PyObjectHashTable.get_item()
# 
# KeyError: 0
# ```

# Similarly, Boolean subsetting always acts like you're using `.loc` (aligning on index values where it can, row order if it can't), and slices in `[]` *always* get behavior like `.iloc`, making behavior much more predictable. 

# ## Getting Columns with Dot-Notation
# 
# In addition to passing the name of a column into `.loc` or to `[]`, columns can also *sometimes* be access using dot-notation: 

# In[6]:


world.country.head()


# This method of getting columns is very easy and intuitive (given how often we use dot-notation in Python more broadly), but it has a couple significant pit-falls:
# 
# - Only works for column names without spaces or punctuation
# - You can't pass a variable to dot-notation, you have to write out the column explicitly (so you can't write generalized code).
# - Only works if the column name isn't the same as an existing method (e.g., `df.count` will call the `count` method, even if you have a column named `"count"`)
# - Can cause problems if you try to put it on the left side of the equals sign. 
# 
# Of these, the reasons for the first and second aren't complicated, but the third and fourth concerns bear exploring. 
# 
# Suppose we added a column to our data called `rank` that gave each country's GDP rank (this code is a little convoluted because there is an easier way to do this, but this works):

# In[7]:


world = world.sort_values("gdppcap08")
world["rank"] = range(0, len(world))
world.head()


# Now watch what happens if we try to access the `rank` column with dot-notation—we don't get the column, we get the method `rank` (that's what `bound method NDFrame.rank` at the top of this output means — it's returning the method, then telling us about the object—our DataFrame—the method is associated with):

# In[8]:


world.rank


# Similar issues arise if you try to assign a column using dot-notation on the *left* side of the assignment operator. For example, suppose we want to shift everyone's rank up by 1:

# In[9]:


# We make an assignment to what we *think* is
# the `rank` column
world.rank = world["rank"] + 1


# In[10]:


world.head()


# It fails silently because what you've actually done is over-written the *method* rank with the column `rank` plus 1. Now now only has your `rank` column not changed (see it still starts with 0), but now you've broken the `rank` method:

# ```python 
# 
# world.rank()
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Cell In[11], line 1
# ----> 1 world.rank()
# 
# TypeError: 'Series' object is not callable
# ```

# And finally, if you try to create a column using dot-notation on the left-hand side of the assignment operator, you will also get into trouble: 

# In[11]:


world.rank_doubled = range(0, 2 * len(world), 2)
world.head()


# See now `rank_doubled` wasn't added to your DataFrame? It just disappears. `pandas` does now raise a warning, but warnings don't stop your code from running, so if you don't see it, you can corrupt your data. 

# **My advice on dot-notation:** 
# 
# - Just don't use dot-notation on the left-hand side of the assignment operator. You're begging for trouble, and just making that a rule means you don't have to worry about when you might be causing a conflict with a method.
# - Try not to use it on the right side of the assignment operator. It's safer than using it on the left side of the assignment operator, but none of us will ever memorize all the names of methods in `pandas`, and if your column happens to have the same name as a method, you may not notice the error. 
