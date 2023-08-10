#!/usr/bin/env python
# coding: utf-8

# # Editing Specific Locations

# In our previous reading, we learned about tools for making global edits on a DataFrame. Those methods are useful for a lot of changes, but sometimes we need more precision than we get from these generalized methods. For example, suppose Mozambique experienced a coup, so we want to set its Polity score to 5. We can't use `replace(15, 5)`, because that would also change the value for Russia, which also has a value of 15 in our data. 
# 
# In these circumstances, we need to directly edit specific locations in our DataFrame. 
# 
# ## Review: Editing Locations in Python and Numpy
# 
# Before diving into how we do this in pandas, though, it may be helpful to review how we do this with other data structures in Python. For example, let's review how to edit an entry in a list with `[]`: 

# In[1]:


my_list = [1, 2, 3]
my_list[2]


# In[2]:


my_list[2] = -42
my_list


# As we can see, when we write `my_list[2]` on the *left* side of the assignment operator (a single equals sign), then whatever we put on the right side of the assignment operator is being assigned *into the entry with index 2* of the list. 
# 
# As you may recall, this same logic can also be extended to two dimensions in `numpy` arrays. Consider the following: 

# In[3]:


import numpy as np

my_array = np.array([[1, 2], [3, 4]])
my_array


# In[4]:


# Edit row 1, column 1
# (recall pandas uses 0-based
# indexing, so `1, 1` is, in 
# normal parlance, the second row
# and second column.

my_array[1, 1] = -42
my_array


# ## Editing Locations in Pandas

# Now that we've had that refresher, we can extend this logic to our `pandas` DataFrames. For example, using `.iloc`, we can make the same kinds of manipulations we just made with a `numpy array`:

# In[5]:


import pandas as pd
df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})
df


# In[6]:


# Edit row 1, column 1. 

df.iloc[1, 1] = -42
df


# But this alone is only kinda useful. After all, our datasets are usually very large, and we rarely want to make modifications to cells whose row numbers we already know. But thankfully, in `pandas` we can pass boolean vectors to `.loc` to identify all rows that meet certain conditions and assign values to those specific cells. For example, suppose we wanted to set column `b` to 0 for all rows where column `a` is even. We could do:

# In[7]:


# Recall that x % 2 gives the remainder after
# dividing x by 2

df.loc[df.a % 2 == 0, "b"] = 0
df


# See how the boolean vector on the left subset for rows where `a` was even (the value of `a % 2` is zero), and the second entry (`b`) subset for the column `b`, then we assigned 0 into those cells? It's just a generalization of the kinds of assignments we did above with lists and numpy arrays, just using boolean vectors and column labels instead of indices!

# Great! But now suppose we don't just want to set certain values to a constant, but instead we wanted to, say, double all the values in odd rows. We can do that to by assigning values that "fit" into the cells on the left of the assignment operator (i.e. by making sure the values we assign have the same dimensions as the cells into which we're trying to assign them):

# In[8]:


df.loc[df.a % 2 == 1, "b"] = df.loc[df.a % 2 == 1, "b"] * 2
df


# ## Our Mozambique Edit
# 
# OK, so let's circle back to our desire to edit our Polity IV value for Mozambique. How would we use this technique here?

# In[9]:


smallworld = pd.read_csv(
    "https://raw.githubusercontent.com/nickeubank/"
    "practicaldatascience/master/Example_Data/world-very-small.csv"
)
smallworld


# In[10]:


smallworld


# Well, we want to put our edit in the row for Mozambique (that's the row index), and put our edit in the column `polityIV`, so:

# In[11]:


smallworld.loc[smallworld.country == "Mozambique", "polityIV"] = 5
smallworld


# Voila!

# And that's how you make precise edits in pandas.

# ## Warning: Chained Assignment
# 
# Note that we've made these edits with `.loc` to specify BOTH the subset of rows we want AND the column we want to edit. It is critically important that when doing these types of edits you use `.loc` to specify both your rows and columns at once. If instead you do these as two separate operations:

# In[12]:


smallworld[smallworld.country == "Mozambique"]["polityIV"] = 5


# You will get the `SettingWithCopyWarning` we discussed in our reading on views and copies. That's because it's possible that when you run `smallworld[smallworld.country == "Mozambique"]`, pandas **may** return an entirely new DataFrame, and the next part of the operation (changing the values of `polityIV`) will run against a completely new DataFrame, not `smallworld`, and in the end your original `smallworld` DataFrame won't end up being modified at all. This kind of chained assignment will SOMETIMES work, but not ALWAYS, which is why you get that warning. 

# ## Categoricals
# 
# A special note is needed to address one oddity of cleaning variables that are of type `Categorical`: `Categorical` variables have a lot of advantages, but they have one annoying feature: you can't insert an arbitrary value into a Categorical. By definition, a Categorical variable can only take on a set number of values.
# 
# To illustrate, let's make our `region` variable into a `Categorical` (in a bigger dataset, it'd be a good candidate for a Categorical, since it only takes on a few string unique values that, in a big dataset, would be repeated a lot):

# In[13]:


smallworld["region"] = pd.Categorical(smallworld["region"])


# Now suppose that Mexico has gotten tired of being in the same region as the United States, and would much prefer to be considered a part of Central America than North America. 
# 
# Normally we could just do `smallworld.loc[smallworld["country"] == "Mexico", "region"] = "C America"`. But if I try that here, because `C America` isn't one of the established values for the Categorical variable, we get this error (with the middle section omitted for brevity):
# 
# ```python
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# /Users/Nick/github/mids_coursera/class_3/week_3/32_cleaning_editing_specific_locations.ipynb Cell 29 in <cell line: 1>()
# ----> 1 smallworld.loc[smallworld["country"] == "Mexico", "region"] = "C America"
# 
# File ~/opt/miniconda3/lib/python3.9/site-packages/pandas/core/indexing.py:716, in _LocationIndexer.__setitem__(self, key, value)
#     713 self._has_valid_setitem_indexer(key)
#     715 iloc = self if self.name == "iloc" else self.obj.iloc
# --> 716 iloc._setitem_with_indexer(indexer, value, self.name)
# 
# [...]
# 
# File ~/opt/miniconda3/lib/python3.9/site-packages/pandas/core/arrays/categorical.py:1484, in Categorical._validate_scalar(self, fill_value)
#    1482     fill_value = self._unbox_scalar(fill_value)
#    1483 else:
# -> 1484     raise TypeError(
#    1485         "Cannot setitem on a Categorical with a new "
#    1486         f"category ({fill_value}), set the categories first"
#    1487     )
#    1488 return fill_value
# 
# TypeError: Cannot setitem on a Categorical with a new category (C America), set the categories first
# ```
# 
# So what do we do?
# 
# One option is to modify the allowable categories for the variable with `.cat.add_categories()`, then making the edit again:

# In[ ]:


smallworld["region"] = smallworld["region"].cat.add_categories(["C America"])
smallworld.loc[smallworld["country"] == "Mexico", "region"] = "C America"


# But if you aren't in a situation where you are REALLY short on RAM or where you REALLY care about the read speed of the variable in question, it's just easier to re-cast the variable to `object` dtype and then work with it normally:

# In[15]:


smallworld["region"] = smallworld["region"].astype("object")
smallworld.loc[smallworld["country"] == "Mexico", "region"] = "C America"


# ## Review
# 
# - Editing individual values can be done using the same type of indexing used for lists and numpy arrays.
# - `.loc` allows for logical tests to enable editing of rows with specific properties.
# - Beware "chained assignment" of the form `df[df["col1"] == "value"]["col2"] = 5`, and heed the warnings it generates.
# - `Categoricals` can be annoying when it comes to editing individual values—to set a value to something that's not currently a category, use `.cat.add_categories` or just re-cast the variable to an `object` dtype. 
